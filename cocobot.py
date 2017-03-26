#!/usr/bin/env python3.6
import json
import regex
import random
import discord
import logging
import asyncio

class Config():
    def __init__(self, app):
        try:
            with open('config/config.json', 'r') as f:
                self.config = json.load(f)
        except Exception as e:
            with open('config/config.json', 'w') as f:
                self.config = dict()
                token = input("Token: ")
                self.config['token'] = token
                json.dump(self.config, f)
    def token(self):
        return self.config['token']
class cocoBot():
    def __init__(self):
        self.client = discord.Client()
        self.config = Config(self)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('discord')
        self.commands = ('kaori', 'cocobot', 'dixionary', 'caori')
bot = cocoBot()
def main():
    bot.logger.info("Starting CocoBot...")
    bot.client.run(bot.config.token())
@bot.client.event
async def on_ready():
    bot.logger.info(f"UserName: {bot.client.user.name}")
    bot.logger.info(f"user ID: {bot.client.user.id}")
@bot.client.event
async def on_message(message):
    recmp = regex.compile("^\;[A-z]+.*")
    if recmp.match(message.content):
        try:
            splitmsg = message.content.split(' ')
            cmd = splitmsg[0].strip(';')
            if cmd in bot.commands:
                tings = (
                        f"Error {bot.client.user.name} started !!!!",
                        f"Error {bot.client.user.name} is borked",
                        f"ERROR OPERATION COMPLETED WITH NO ERRORS",
                        f"Error {bot.client.user.name} failed to change its name",
                        f"Error no errors where found !!!"
                        )
                numb = random.randint(0, len(tings) - 1)
                msg = tings[numb]
                await bot.client.send_message(message.channel, msg)
        except Exception as e:
            bot.logger.error(e)

if __name__ == "__main__":
    main()
