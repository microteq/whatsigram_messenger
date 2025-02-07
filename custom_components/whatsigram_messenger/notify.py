"""Module for setting up a recipient entity.

Author: D. Geisenhoff
Created: 24-JAN-2025
"""

# ***********************************************************************************************************************************************
# Purpose:  Module for setting up and handling the Whatsigram Messenger service in Home Assistant
# History:  D.Geisenhoff    23-OCT-2024     Created
# ***********************************************************************************************************************************************

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_NAME, CONF_URL, DOMAIN, GLOBAL_COUNTER


# ***********************************************************************************************************************************************
# Purpose:  Setup messenger recipient (runs when Home Assist is started or when the integration is added)
# History:  D.Geisenhoff    24-JAN-2025     Created
# ***********************************************************************************************************************************************
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up the CallMeBot api."""
    entity = WhatsigramEntity(hass,entry)
    async_add_entities([entity])


# ***********************************************************************************************************************************************
# Purpose:  Recipient entity class
# History:  D.Geisenhoff    24-JAN-2025     Created
# ***********************************************************************************************************************************************
class WhatsigramEntity(Entity):
    """Class for single switch entity (one relay)."""

    # ***********************************************************************************************************************************************
    # Purpose:  Initialize a recipient entity
    # History:  D.Geisenhoff    28-JAN-2025     Created
    # ***********************************************************************************************************************************************
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize notification target."""
        self.entry = entry
        self.entity_id = f"notify.whatsigram_recipient_{hass.data[DOMAIN][GLOBAL_COUNTER]}"
        self.state = 'ready'
        self._is_enabled = True
        self._attr_available = True
        self._attr_has_entity_name = False
        self._attr_name="Whatsigram " + entry.data[CONF_NAME]
        self._attr_unique_id = f"{entry.entry_id}"
        self._attr_icon  = "mdi:message-outline"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            model="Whatsigram Messenger",
            name = "Whatsigram " + entry.data[CONF_NAME]
        )


    # ***********************************************************************************************************************************************
    # Purpose:  Send a message to a recipient
    # History:  D.Geisenhoff    28-JAN-2025     Created
    # ***********************************************************************************************************************************************
    async def _async_send_message(self, message: str = "", **kwargs: Any) -> None:
        """Send a message to a recipient."""
        self.state = 'sending'
        api = self.hass.data[DOMAIN]['api']
        url = self.entry.data[CONF_URL]
        await api.send_message(message, url)
        self.state = 'ready'

