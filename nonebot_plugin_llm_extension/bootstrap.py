from typing import TYPE_CHECKING, cast

from nonebot import logger
from nonebot import get_driver, Driver as BaseDriver
from nonebot.drivers import HTTPClientMixin

from .config import config

driver = get_driver()

plugin_enable = True

api_key = config.api_key

if not api_key:
    plugin_enable = False
    logger.error("缺失必要配置项，已禁用该插件")

if not isinstance(driver, HTTPClientMixin):
    plugin_enable = False
    raise RuntimeError("Driver must be HTTPClientMixin")


if TYPE_CHECKING:

    class Driver(BaseDriver, HTTPClientMixin): ...

    driver = cast(Driver, driver)
