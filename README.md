# Whatsigram Messenger: Integration for Home Assistant
**Sending messages from Home Assistant to Whatsapp, Signal or Telegram.**

The Whatsigram Messenger is an integration for Home assistant allowing you to send messages, notifications or alerts to your preferred messenger on your mobile phone. Whatsigram can send messeges to the Whatsapp, Signal or Telegram App using the free CallMeBot service.

## Preparing your mobile phone

Die Vorbereitung auf deinem Mobiltelefon ist für jede App ein wenig anders, aber immer sehr einfach zu machen. Sie dient dazu, CallMeBot zu erlauben, dir Nachrichten zu senden und deinen Account vor Spam zu schützen.

### Whatsapp

- Add the phone number **+34 644 52 74 88** into your Phone Contacts. (Name it as you wish)
- In your Whatsapp App, send the message **I allow callmebot to send me messages** to the new Contact created

The bot will answer with your personal api key and an URL, you can use to send messages to yoursaelf through CallMeBot.

**Please note that using the CallMeBot service sending to Whatsapp is only free for personal use.**

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) website.

### Signal

- Add the phone number **+34 644 52 74 88** into your Phone Contacts. (Name it as you wish)
- In your Signal App, send the message **I allow callmebot to send me messages** to the new Contact created

The bot will answer with your personal api key and an URL, you can use to send messages to yoursaelf through CallMeBot.

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/free-api-signal-send-messages/) website.

### Telegram

Du kannst versuchen, in deiner Telegram App den Text **/start** an **@CallMeBot_txtbot** zu senden und dann auf der CallmeBot Seite eine [Testnachricht zu senden](https://www.callmebot.com/blog/telegram-text-messages-from-browser/#google_vignette). Sollte dein Account dann noch nicht für CallMeBot freigegeben sein, dann kannst du dich über [desem Link](https://api2.callmebot.com/txt/login.php) einloggen und CallMeBot damit die Erlaubnis erteilen, dir Nachrichten zu senden.

For more details, please refer to the [CallMeBot](https://www.callmebot.com/blog/telegram-text-messages/) website.


## Installation


## Configuration

In your Home Assistant go to **Settings** > **Devices & services** and click on **Add integration**. In the search field, search for **whatsigram** and select the integration. This will add a recipient entity, you can use to send notifications to. In the name field, you can enter the recipients name or phone number or whatever you wish.

### Whatsapp

In the URL field, copy the exact URL as you received it from CallMeBot in response to your Whatsapp request.

### Signal

In the URL field, copy the exact URL as you received it from CallMeBot in response to your Signal request.

### Telegram

Copy the URL `https://api.callmebot.com/text.php?user=@yourusername&text=Text` into the URL field and replace **@yourusername** with your Telegram user name.


Before submitting the form, you can tick the _Send a test message_ check box to test your url, you have entered.

After having added your integration, you can add more recipients, if needed. Click on your _Whatsap Messenger integration_ and then click on _add entry_. Du kanns jede aArt Empfänger hinzufügen, sei es für Whatapp, Signal oder Telegram, solange der Empfänger sein Mobiltelefon für den Empfang von CallMeBot Nachrichen vorbereitet hat.

## Usage

