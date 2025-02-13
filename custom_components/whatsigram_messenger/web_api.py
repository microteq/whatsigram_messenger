"""Web API class."""

import asyncio
import logging
from urllib.parse import quote_plus

import aiohttp
from aiohttp import ClientTimeout
import requests

from homeassistant.core import HomeAssistant

from .const import (
    ERROR_CONNECTION_FAILED,
    ERROR_INVALID_KEY,
    ERROR_NO_RECIPIENT,
    ERROR_NO_TEXT,
    ERROR_PAGE_NOT_FOUND,
    ERROR_PERMISSION_DENIED,
    ERROR_TEMP_UNAVAILABLE,
    ERROR_UNKNOWN,
    ERROR_WRONG_PARAMETER,
)

_LOGGER = logging.getLogger(__name__)


# ***********************************************************************************************************************************************
# Purpose:  CallMeBot Web API class
# History:  D.Geisenhoff    24-OCT-2024     Created
# ***********************************************************************************************************************************************
class WebAPI:
    """CallMeBot Web API class."""

    # ***********************************************************************************************************************************************
    # Purpose:  Initialize the class
    # History:  D.Geisenhoff    24-OCT-2024     Created
    # ***********************************************************************************************************************************************
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the class."""
        self.hass = hass

    @property
    def test(self):
        """Check if relay is available."""
        return "ok"

    # ***********************************************************************************************************************************************
    # Purpose:  Send a message
    # History:  D.Geisenhoff    29-JAN-2025     Created
    # ***********************************************************************************************************************************************
    async def send_message(self, message: str, url: str) -> str:
        """Send a message using the provided configuration entry."""
        url_with_message = url
        position = url.lower().find("&text=")
        if position != -1:
            # Find the text parameter and replace it by the user message
            url_with_message = url[:position] + "&text=" + quote_plus(message)
            position_amp = url.find("&", position + 1)
            if position_amp != -1:
                url_with_message += url[position_amp:]
        async with aiohttp.ClientSession() as session:
            try:
                for i in range(11):
                    async with session.get(url_with_message, timeout=ClientTimeout(connect=30)) as response:
                        if response.status == 200:
                            content = await response.text()
                            content = content.lower()
                            # Signal:Message sent, Whatsapp: Message queued, Telegram: Successful
                            if "message sent" in content or "message queued" in content or "successful" in content:
                                break
                            if "no user specified" in content:
                               # Telegram: no user specified
                                _LOGGER.error("No recipient has been specified.")
                                return ERROR_NO_RECIPIENT
                            if "no text specified" in content or "text/image parameter is missing" in content:
                               # No text specified
                                _LOGGER.error("No text has been specified.")
                                return ERROR_NO_TEXT
                            if "apikey is invalid" in content:
                               # Signal: Invalid API key
                                _LOGGER.error("Invalid API key.")
                                return ERROR_INVALID_KEY
                            if "permission denied" in content:
                               # Telegram: user permission denied
                                _LOGGER.error("Permission denied. You need to authorize CallMeBot to contact this user.")
                                return ERROR_PERMISSION_DENIED
                            _LOGGER.error("Unknown error: %s", content)
                            return ERROR_UNKNOWN
                        if response.status == 503:
                            # Wait if service is not available (CallMeBot does not allow too many messages at a time)
                            if i == 11:
                                _LOGGER.error("CallMeBot service temporary not availavle / timeout")
                                return ERROR_TEMP_UNAVAILABLE
                            await asyncio.sleep(10)
                        elif response.status == 201:
                            # Whatsapp: invalid API key
                            _LOGGER.error("Invalid or no recipient, or no text specified")
                            return ERROR_WRONG_PARAMETER
                        elif response.status == 203:
                            # Whatsapp: invalid API key
                            _LOGGER.error("Invalid API key or recipient")
                            return ERROR_WRONG_PARAMETER
                        elif response.status == 404:
                            # CallMeBot page not found
                            _LOGGER.error("Page not found")
                            return ERROR_PAGE_NOT_FOUND
                        else:
                            _LOGGER.error("Unknown error")
                            return ERROR_UNKNOWN
            except aiohttp.ClientError as err:
                _LOGGER.error("Unable to connect to the CallMeBot service: %s", err)
                return ERROR_CONNECTION_FAILED
            except TimeoutError as ex:
                _LOGGER.error("Request to CallMeBot service timed out: %s", ex)
                return ERROR_TEMP_UNAVAILABLE
            except Exception as ex:
                _LOGGER.error("An unexpected error occurred: %s", ex)
                return ERROR_UNKNOWN
        return "ok"
