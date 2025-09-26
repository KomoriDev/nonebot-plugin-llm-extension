from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")

from .config import Config
from .extension import LLMExtension as LLMExtension

__version__ = "0.1.1"
__plugin_meta__ = PluginMetadata(
    name="言令",
    description="利用 LLM 将自然语言转换为机器人指令",
    usage="详见文档",
    type="library",
    homepage="https://github.com/KomoriDev/nonebot-plugin-llm-extension",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={
        "unique_name": "LLM Extension",
        "author": "Komorebi <mute231010@gmail.com>",
        "version": __version__,
    },
)
