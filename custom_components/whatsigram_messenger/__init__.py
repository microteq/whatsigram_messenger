"""Module for setting up the Whatsigram Messenger in Home Assistant.

This module sets up the messenger and provides functionality to send messages
via the CallMeBot API when Home Assistant is started or when the integration is added.

Author: D. Geisenhoff
Created: 24-JAN-2025
"""

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er

from .const import (
    CONF_NAME,
    CONF_TEST,
    CONF_URL,
    DOMAIN,
    GLOBAL_API,
    GLOBAL_COUNTER,
    PLATFORMS,
)
from .web_api import WebAPI

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_URL): str,
                vol.Optional(CONF_TEST): bool,
            }
        )
    }
)

# ***********************************************************************************************************************************************
# Purpose:  Setup when Home Assistant starts, can run after or before setup_entry
# History:  D.Geisenhoff    29-JAN-2025     Cfreated
# ***********************************************************************************************************************************************
async def async_setup(hass, config):
    """Set up the component."""
    return True


# ***********************************************************************************************************************************************
# Purpose:  Initialize global variables
# History:  D.Geisenhoff    29-JAN-2025     Cfreated
# ***********************************************************************************************************************************************
def init_vars(hass: HomeAssistant):
    """Initialize global variables for the Whatsigram Messenger component."""
    if DOMAIN not in hass.data:
        hass.data.setdefault(DOMAIN, {})
        hass.data[DOMAIN][GLOBAL_API] = WebAPI(hass)
    # Set a global counter for the entity id (entity id should change after entity has been created, so the name of the recipient cannot be taken)
    # The entity id will be notify_whatsigram_recipient_1, ...recipient_2, ...
    if GLOBAL_COUNTER not in hass.data[DOMAIN]:
        hass.data[DOMAIN][GLOBAL_COUNTER] = 1
    else:
        hass.data[DOMAIN][GLOBAL_COUNTER] += 1


# ***********************************************************************************************************************************************
# Purpose:  Setup entities. Run when Home Assist is started, or entry is added. Can run after or before setup
# History:  D.Geisenhoff    29-JAN-2025     Cfreated
# ***********************************************************************************************************************************************
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the entry."""

    init_vars(hass)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    # Add a listener for config changes and remove when entity is unloaded
    entry.async_on_unload(entry.add_update_listener(async_update_options))
    return True


# ***********************************************************************************************************************************************
# Purpose:  Update entity name, when configuration changes
# History:  D.Geisenhoff    29-JAN-2025     Created
# ***********************************************************************************************************************************************
async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update entity name."""
    entity_reg = er.async_get(hass)
    entities = er.async_entries_for_config_entry(entity_reg, entry.entry_id)
    entity_reg.async_update_entity(entities[0].entity_id, name="Whatsigram " + entry.data[CONF_NAME])


# ***********************************************************************************************************************************************
# Purpose:  Called when entry is unloaded
# History:  D.Geisenhoff    23-OCT-2024     Created
# ***********************************************************************************************************************************************
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload the entry."""
    config_entries = hass.config_entries.async_entries(DOMAIN)
    if len(config_entries) == 1:
        hass.data.pop(DOMAIN)
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
