"""
shellog.

A Python package to get notifications about the logs of a process.
"""

__version__ = "1.0.2"
__author__ = 'Daniele Margiotta'
__credits__ = 'Reveal s.r.l.'

import telebot

class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot('token_bot')
        self.chat_id = []

    def sendMessage(self, text: str):
        for id in self.chat_id:
            self.bot.send_message(id, text)
            
    def addChatId(self, id: str):
        self.chat_id.append(id)
    
    def addListChatIds(self, ids):
        for id in ids:
            self.chat_id.append(id)
    
    def removeChatId(self, id:str):
        self.chat_id.remove(id)

    def removeListChatIds(self, ids):
        for id in ids:
            self.chat_id.remove(id)
    
    def clearChatId(self):
        self.chat_id.clear()

bot = Bot()

