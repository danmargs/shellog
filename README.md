# Shellog 1.0.2
Have you ever needed to monitor your background processes when you couldn't access your PC or VPN?

Shellog empowers you to seamlessly integrate logs into your Python code, delivering direct notifications to your Telegram chat. Additionally, for teams, it facilitates log sharing.

The primary aim of the Shellog library is to streamline process monitoring, and we'll explore how it accomplishes this with ease.

# Requirements
1. Connect to your Telegram account: https://web.telegram.org/
2. Join the chat: https://t.me/shellogbot
3. Set the ChatId:  
   a. Type `/id` into the chat  
   b. Save for later the *ChatId* returned  

# Installation
```shell
pip install shellog
```

# Use Case
```python
# Import library
import shellog

# Instantiate bot
b = shellog.Bot()

# Set the ChatId or the ChatIds (notice that a ChatId is a string type)
b.addChatId("ChatId")
b.addListChatIds(["ChatId_1", "ChatId_2", ...])

# Remove the ChatId or the ChatIds (notice that a ChatId is a string type)
b.removeChatId("ChatId")
b.removeListChatIds(["ChatId_1", "ChatId_2", ...])
        
# Send log message 
b.sendMessage(*"Hey! I'm here!"*)
```
