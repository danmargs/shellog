Shellog 1.0.2
=============================
Have you ever needed to monitor your background processes when you couldn't access your PC or VPN?

Shellog empowers you to seamlessly integrate logs into your Python code, delivering direct notifications to your Telegram chat. Additionally, for teams, it facilitates log sharing.

The primary aim of the Shellog library is to streamline process monitoring, and we'll explore how it accomplishes this with ease.

Requirements
=============================
    *   Connect to your Telegram account
        1. https://web.telegram.org/
        
    *   Join the chat
        1. https://t.me/shellogbot
        
    *   Set the ChatId
        1. type /id into the chat
        2. pin the *ChatId* returned

Installation
=============================
    *   Shellog
        1. pip install shellog

Use Case
=============================
    *   Import library
        1. import shellog
        
    *   Instantiate bot
        1. b = shellog.Bot()
        
    *   Set the ChatId or the ChatIds (notice that a ChatId is a string type)
        1. b.addChatId("ChatId")
        2. b.addListChatIds(["ChatId_1", "ChatId_2", ...])
        
    *   Remove the ChatId or the ChatIds (notice that a ChatId is a string type)
        1. b.removeChatId("ChatId")
        2. b.removeListChatIds(["ChatId_1", "ChatId_2", ...])
        
    *   Send log message 
        1. b.sendMessage(*"Hey! I'm here!"*)
