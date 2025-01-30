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
CONF_TEST = "test_connection"

ERROR_CONNECTION_FAILED = "connection_error"
ERROR_PERMISSION_DENIED = "permission_denied"
ERROR_INVALID_URL = "invalid_url"
ERROR_INVALID_KEY = "invalid_key"
ERROR_PAGE_NOT_FOUND = "404"
ERROR_TEMP_UNAVAILABLE = "503"
ERROR_NO_RECIPIENT = "no_recipient"
ERROR_NO_TEXT = "no_text"
ERROR_WRONG_PARAMETER = "wrong_parameter"
ERROR_UNKNOWN = "unknown"
