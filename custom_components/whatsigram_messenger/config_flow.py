# ***********************************************************************************************************************************************
# Purpose:  Config flow for the Whatsigram Messenger integration.
# History:  D.Geisenhoff    30-JAN-2025     Created
# ***********************************************************************************************************************************************
"""Config flow for the Whatsigram Messenger integration."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import CONF_NAME, CONF_TEST, CONF_URL, DOMAIN, GLOBAL_API
from .web_api import WebAPI


# ***********************************************************************************************************************************************
# Purpose:  Send a test message
# History:  D.Geisenhoff    30-JAN-2025     Created
# ***********************************************************************************************************************************************
async def _test_connection(hass, user_input) -> str:
    """Test the connection with the provided user input."""
    if DOMAIN not in hass.data:
        hass.data.setdefault(DOMAIN, {})
        hass.data[DOMAIN][GLOBAL_API] = WebAPI(hass)
    api = hass.data[DOMAIN][GLOBAL_API]
    return await api.send_message("Test message", user_input[CONF_URL])


# ***********************************************************************************************************************************************
# Purpose:  Configurationn form for the integration (runs when integration entry is added)
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
                    vol.Optional(CONF_TEST): bool,
                }),
            )
        # User has clicked on submit
        errors = {}
        result = "ok"
        if user_input.get("test_connection"):
            # Send a test message
            result = await _test_connection(self.hass, user_input)
        if result == "ok":
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
        errors["base"] = result
        # Show form with user entered data
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME,
                        default=user_input[CONF_NAME],
                    ): str,
                    vol.Required(
                        CONF_URL,
                        default=user_input[CONF_URL],
                    ): str,
                    vol.Optional(CONF_TEST): bool,
                }
            ),
            errors = errors
        )


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
# Purpose:  Configuration form for options (runs when configuration link is clicked)
# History:  D.Geisenhoff    24-JAN-2025     Created
# ***********************************************************************************************************************************************
class WhatsigramOptionsFlow(config_entries.OptionsFlow):
    """Show form for configuring an existing integration entry."""

    # ***********************************************************************************************************************************************
    # Purpose:  Initialize the class.
    # History:  D.Geisenhoff    25-JAN-2025     Created
    # ***********************************************************************************************************************************************
    def __init__(self, config_entry) -> None:
        """Initialize the class."""
        self._config_entry = config_entry
        self._old_config_data = config_entry.data.copy()


    # ***********************************************************************************************************************************************
    # Purpose:  Show first (and in this case only) step of config form
    # History:  D.Geisenhoff    25-JAN-2025     Created
    # ***********************************************************************************************************************************************
    async def async_step_init(self, user_input=None):
        """Show first (and in this case only) step of config form."""
        if user_input is None:
            # Show form with data from config_entry
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
                        ): str,
                        vol.Optional(CONF_TEST): bool,
                    }
                )
            )
        errors = {}
        result = "ok"
        if user_input.get("test_connection"):
            # Send a test message
            result = await _test_connection(self.hass, user_input)
        if result == "ok":
            # merge user_input and config_entry.data into new dictionary
            new_data = {**self._config_entry.data, **user_input}
            # async_update_entry saves the new changes
            self.hass.config_entries.async_update_entry(self._config_entry, data=new_data, title = user_input[CONF_NAME])
            return self.async_create_entry(title="", data={})
        errors["base"] = result
        # Show form with user entered data
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME,
                        default=user_input[CONF_NAME],
                    ): str,
                    vol.Required(
                        CONF_URL,
                        default=user_input[CONF_URL],
                    ): str,
                    vol.Optional(CONF_TEST): bool,
                }
            ),
            errors = errors
        )

