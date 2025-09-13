from __future__ import annotations

import asyncio
from tarina import LRU
from nonebot.log import logger
from nonebot.adapters import Bot, Event
from arclet.alconna.tools import ShellTextFormatter
from nonebot_plugin_alconna import Alconna, Extension, UniMessage, get_message_id

from .config import config
from .bootstrap import driver
from ._client import LLMClient


class LLMExtension(Extension):
    _command_registry: list[Alconna] = []
    _handled_messages: LRU[str, asyncio.Future] = LRU(20)

    @property
    def priority(self) -> int:
        return 15

    @property
    def id(self) -> str:
        return "LLMExtension"

    def __init__(self):
        self.llm = LLMClient(config.base_url, config.api_key, config.model)
        driver.on_startup(self._initialize_llm)

    def post_init(self, alc: Alconna) -> None:
        if alc not in self._command_registry:
            self._command_registry.append(alc)

    def _initialize_llm(self) -> None:
        formatter = ShellTextFormatter()
        for command in self._command_registry:
            formatter.add(command)

        full_help = formatter.format_node()
        self.llm.build_prompt(commands_help=full_help)

    async def receive_wrapper(
        self,
        bot: Bot,
        event: Event,
        command: Alconna,
        receive: UniMessage,
    ):
        message_id = get_message_id(event, bot)
        if message_id in self._handled_messages:
            return await self._handled_messages[message_id]

        future = asyncio.Future()
        self._handled_messages[message_id] = future

        try:
            resp = await self.llm.input(str(receive))
            content = resp["choices"][0]["message"]["content"]
            output = UniMessage(content)
            future.set_result(output)

            if str(output) != str(receive):
                logger.info(f"Message transformed: {receive} → {output}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            future.set_result(receive)

        return await future
