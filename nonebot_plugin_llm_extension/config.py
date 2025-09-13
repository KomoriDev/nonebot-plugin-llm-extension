from pydantic import Field, BaseModel
from nonebot import get_plugin_config


class ScopedConfig(BaseModel):
    base_url: str = "https://api.deepseek.com/v1"
    """LLM Endpoint"""
    api_key: str = ""
    """API Key"""
    model: str = "deepseek-reasoner"
    """Model Name"""

    only_alconna: bool = True
    """Only respond to Alconna commands"""


class Config(BaseModel):
    llm_extension: ScopedConfig = Field(default_factory=ScopedConfig)
    """LLM Extension Config"""


config = get_plugin_config(Config).llm_extension
