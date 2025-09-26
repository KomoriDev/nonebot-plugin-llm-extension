import json
from nonebot.drivers import Request

from .bootstrap import driver

system_prompt_template = """
你是一个智能机器人助手，能够理解用户的意图，并将口语化的消息转换为机器人指令。
你的任务是识别用户想要执行的命令，并将其转换为对应的 Alconna 命令格式。

指令前缀为: {command_start}。

以下是可用的指令列表及其详细帮助信息：

{commands_help}

如果用户的意图无法匹配任何命令，请返回原消息。
---
现在请根据用户的输入，转换成对应的命令。
"""


class LLMClient:
    def __init__(self, endpoint: str, api_key: str, model: str):
        self.endpoint = endpoint
        self.api_key = api_key
        self.model = model

        self.session = driver.get_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc_info):
        await self.close()

    async def close(self):
        await self.session.close()

    def _build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def build_prompt(self, commands_help: str):
        self.system_prompt = system_prompt_template.format(
            command_start=driver.config.command_start, commands_help=commands_help
        )

    async def input(self, message: str, **kwargs) -> dict:
        url = f"{self.endpoint}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message},
            ],
            "stream": False,
            **kwargs,
        }

        response = await self.session.request(
            Request("POST", url, headers=self._build_headers(), json=payload)
        )

        assert response.content

        return json.loads(response.content)
