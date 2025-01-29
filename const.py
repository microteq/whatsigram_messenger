"""Constants for the Whatsigram Messenger integration."""

import logging

from homeassistant.const import Platform

logging.basicConfig(format="%(message)s")

DOMAIN = "whatsigram_messenger"
PLATFORMS: list[Platform] = [Platform.NOTIFY]

GLOBAL_API = "api"
GLOBAL_COUNTER = "counter"

CONF_NAME = "name"
CONF_URL = "url"
