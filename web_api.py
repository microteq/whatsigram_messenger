"""Web API class."""

import asyncio
import logging
from urllib.parse import quote_plus

import aiohttp
from aiohttp import ClientTimeout

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_URL

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


    # ***********************************************************************************************************************************************
    # Purpose:  Test connection
    # History:  D.Geisenhoff    24-OCT-2024     Created
    # ***********************************************************************************************************************************************
    # async def test_connection(self) -> bool:
    #     try:
    #         async with self.session.get(
    #             f"http://{self.host}/cm?cmnd=Status%200",
    #             timeout=ClientTimeout(connect=3),
    #         ) as response:
    #             return response.status == 200
    #     except aiohttp.ClientError:
    #         return False


    # ***********************************************************************************************************************************************
    # Purpose:  Send a message
    # History:  D.Geisenhoff    29-JAN-2025     Created
    # ***********************************************************************************************************************************************
    async def send_message(self, message: str, entry: ConfigEntry) -> None:
        """Send a message using the provided configuration entry."""
        url = entry.data[CONF_URL]
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
                for _ in range(10):
                    async with session.get(url_with_message, timeout=ClientTimeout(connect=3)) as response:
                        if response.status == 200:
                            break
                        if response.status == 503:
                            # Wait if service is not available (CallMeBot does not allow too many messages at a time)
                            await asyncio.sleep(10)
                        else:
                            _LOGGER.error("Invalid Web API command: %s", url_with_message)
                            return "invalid"
            except aiohttp.ClientError as err:
                _LOGGER.warning("Unable to connect to the CallMeBot service: %s", err)
                return "error"
        return "ok"
