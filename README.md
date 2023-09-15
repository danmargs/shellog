Shellog
=============================
Have you ever needed to monitoring of your background processes when you didn't have the ability to access the pc or vpn?

**Shellog** gives you the ability to be able to insert logs within your Python code that will notify you directly on a **Telegram chat**.
Also if you are a Team it will provide you with the ability to be able to share logs.

The goal of the library **Shellog** is to allow monitoring of processes with simplicity, let's see how it will be possible to do this.

Requirements
=============================
    *   Connect to your Telegram account
        1. https://web.telegram.org/
    *   Join the chat
        1. https://t.me/shellogbot
    *   Set the ChatId
        1. type */id* into the chat
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
    *   Set the ChatId or the ChatIds
        1. b.addChatId(*ChatId*)
        1. b.addListChatIds([*ChatId_1*, *ChatId_2*, ...])
    *   Remove the ChatId or the ChatIds
        1. b.removeChatId(*ChatId*)
        1. b.removeListChatIds([*ChatId_1*, *ChatId_2*, ...])
    *   Send log message 
        1. b.sendMessage(*"Hey! I'm here!"*)
