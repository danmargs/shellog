"""
shellog.

A Python package to get notifications about the logs of a process.
"""

__version__ = "1.0.0"
__author__ = 'Daniele Margiotta'
__credits__ = 'Reveal s.r.l.'

import telebot

class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot('6300373442:AAEeMHpIq_ttEGdmQzE04706UR0rJISCSHM')
        self.chat_id = ""

    def sendMessage(self, text: str):
        if self.chat_id != "":
            self.bot.send_message(self.chat_id, text)
        else:
            print("Chat Id unset, please start the ChatBot and send the command /id, after that call the function setChatId()")
    
    def setChatId(self, id: str):
        self.chat_id = id
    
bot = Bot()

