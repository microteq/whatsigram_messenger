"""Config flow for the Whatsigram Messenger integration."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import CONF_NAME, CONF_URL, DOMAIN


# ***********************************************************************************************************************************************
# Purpose:  Configurationn form for integration (run when integration entry is added)
# History:  D.Geisenhoff    24-JAN-2025     Created
# ***********************************************************************************************************************************************
class WhatsigramConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Whatsigram Messenger."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle the initial step of the config flow."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): str,
                    vol.Required(CONF_URL): str,
                }),
            )
        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)


    # ***********************************************************************************************************************************************
    # Purpose:  Callback from options flow (must be inside class, otherwise the 'Configuration' link will not be displayed)
    # History:  D.Geisenhoff    24-JAN-2025     Created
    # ***********************************************************************************************************************************************
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Configure additional options."""
        return WhatsigramOptionsFlow(config_entry)


# ***********************************************************************************************************************************************
# Purpose:  Configuration form class (run when configuration link is clicked)
# History:  D.Geisenhoff    24-JAN-2025     Created
# ***********************************************************************************************************************************************
class WhatsigramOptionsFlow(config_entries.OptionsFlow):
    """Show form for configuring an existing integration entry."""

    # ***********************************************************************************************************************************************
    # Purpose:  Initialize the class.
    # History:  D.Geisenhoff    24-OCT-2025     Created
    # ***********************************************************************************************************************************************
    def __init__(self, config_entry) -> None:
        """Initialize the class."""
        self._config_entry = config_entry
        self._old_config_data = config_entry.data.copy()


    # ***********************************************************************************************************************************************
    # Purpose:  Show first (and in this case only) step of config form
    # History:  D.Geisenhoff    25-OCT-2024     Created
    # ***********************************************************************************************************************************************
    async def async_step_init(self, user_input=None):
        """Show first (and in this case only) step of config form."""
        if user_input is None:
            return self.async_show_form(
                step_id="init",
                data_schema=vol.Schema(
                    {
                        vol.Required(
                            CONF_NAME,
                            default=self._config_entry.data.get(CONF_NAME),
                        ): str,
                        vol.Required(
                            CONF_URL,
                            default=self._config_entry.data.get(CONF_URL),
                        ): str
                    }
                ),
            )
        # merge user_input and config_entry.data into new dictionary
        new_data = {**self._config_entry.data, **user_input}
        # async_update_entry saves the new changes
        self.hass.config_entries.async_update_entry(self._config_entry, data=new_data, title = user_input[CONF_NAME])
        return self.async_create_entry(title="", data={})

