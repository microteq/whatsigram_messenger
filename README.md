# Whatsigram Messenger: Integration for Home Assistant
**Sending messages from Home Assistant to Whatsapp, Signal or Telegram.**

The Whatsigram Messenger is an integration for Home assistant allowing you to send messages, notifications or alerts to your preferred messenger on your mobile phone. Whatsigram can send messeges to the Whatsapp, Signal or Telegram App using the free CallMeBot service.
<br>
<br>
## Preparing your mobile phone

Die Vorbereitung auf deinem Mobiltelefon ist für jede App ein wenig anders, aber immer sehr einfach zu machen. Sie dient dazu, CallMeBot zu erlauben, dir Nachrichten zu senden und deinen Account vor Spam zu schützen.

### Whatsapp

- Add the phone number **+34 644 52 74 88** into your Phone Contacts. (Name it as you wish)
- In your Whatsapp App, send the message **I allow callmebot to send me messages** to the new Contact created

The bot will answer with your personal api key and an URL, you can use to send messages to yoursaelf via CallMeBot.

**Please note that using the CallMeBot service sending to Whatsapp is only free for personal use.**

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) website.

### Signal

- Add the phone number **+34 644 52 74 88** into your Phone Contacts. (Name it as you wish)
- In your Signal App, send the message **I allow callmebot to send me messages** to the new Contact created

The bot will answer with your personal api key and an URL, you can use to send messages to yoursaelf via CallMeBot.

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/free-api-signal-send-messages/) website.

### Telegram

You can try sending the text **/start** to **@CallMeBot_txtbot** in your Telegram app and then send a [test message](https://www.callmebot.com/blog/telegram-text-messages-from-browser/#google_vignette) on the CallMeBot page. If then your account is still not approved for CallMeBot, you can log in via [this link](https://api2.callmebot.com/txt/login.php) and give CallMeBot permission to send you messages.

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/telegram-text-messages/) website.
<br>
<br>
## Installation
<!--
### HACS (recommended)
<a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=microteq&amp;repository=whatsigram_messenger&amp;category=integration" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store."></a>

This is the recommended installation method.

- Search for and install the Whatsigram Messenger integration from HACS
- Restart Home Assistant
-->
### Manual
- Download the latest release
- Copy the contents of custom_components into the /config/custom_components directory of your Home Assistant installation
- Restart Home Assistant
<br>

## Configuration

In your Home Assistant go to _Settings_ > _Devices & services_ and click on _Add integration_. In the search field, search for _whatsigram_ and select the integration. This will add a recipient entity, you can use to send notifications to. In the name field, you can enter the recipients name or phone number or whatever you wish.

### Whatsapp

In the URL field, copy the exact URL as you received it from CallMeBot in response to your Whatsapp request.

### Signal

In the URL field, copy the exact URL as you received it from CallMeBot in response to your Signal request.

### Telegram

Copy the URL `https://api.callmebot.com/text.php?user=@myusername&text=Text` into the URL field and replace **@myusername** with your Telegram user name.
<br>
<br>
<br>
Before submitting the form, you can tick the _Send a test message_ check box to test your url, you have entered.

After having added your integration, you can add more recipients, if needed. Click on your _Whatsap Messenger integration_ and then click on _add entry_. You can add any type of recipient, whether for WhatsApp, Signal, or Telegram, as long as the recipient has prepared their mobile phone to receive CallMeBot messages.
<br>
<br>
## Usage

The Whatsigram integration creates recipient entities to which standard notifications can be sent. In Home Assistant, sending a message is typically used as an action in an automation.

So in your automation, click on _Add action_, then on _Notifications,_ and select the action _Send a notification message_. In the _Message_ field, enter your message, and as _Target_, click on _Choose entity_ and select one (or more) Whatsigram recipient(s). Then save your action.
<br />
<br />

## License

This integration is published under the GNU General Public License v3.0.
<br />
<br />
<br />
<br />
<br />
<br />

## About sponsorship


If this Home Assistant integration has been helpful to you, I’d be grateful for your support. Sponsorship helps me keep the project going, improve features, and fix any issues that arise. Your contribution goes a long way in making the project better for everyone.

Thanks for considering!

[![Sponsor me on GitHub](https://img.shields.io/badge/sponsor-me%20on%20GitHub-green)](https://github.com/sponsors/microteq)

<a href="https://www.buymeacoffee.com/microteq" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 38px !important;width: 140px !important;" ></a>









