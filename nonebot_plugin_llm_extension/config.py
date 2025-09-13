from pydantic import Field, BaseModel
from nonebot import get_plugin_config


class ScopedConfig(BaseModel): ...


class Config(BaseModel):
    llm_extension: ScopedConfig = Field(default_factory=ScopedConfig)
    """LLM Extension Config"""


plugin_config = get_plugin_config(Config).llm_extension
