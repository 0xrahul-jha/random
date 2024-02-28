import discord
import os
import random
import re
import sqlite3
from gmresponses import gm_database
from helloresponses import hello_database

intents = discord.Intents.all()

# Call the gm_database and hello_database functions to initialize the respective databases
gm_database()
hello_database()

conn_gm = sqlite3.connect('gm-responses.db')
cursor_gm = conn_gm.cursor()

conn_hello = sqlite3.connect('hello-responses.db')
cursor_hello = conn_hello.cursor()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id or message.mentions:
            return

        gm_greetings_pattern = re.compile(
            r'(\bgm\b|\bmorning\b|\bgood\s?morning\b)', re.IGNORECASE)
        if gm_greetings_pattern.search(message.content):
            cursor_gm.execute(
                "SELECT response_text FROM responses_table ORDER BY RANDOM() LIMIT 1"
            )
            response = cursor_gm.fetchone()[0]
            await message.reply(response, mention_author=True)
        else:
            hello_greetings_pattern = re.compile(
                r'(\bhi\b|\bhello\b|\bhey\b|\bhola\b)', re.IGNORECASE)
            if hello_greetings_pattern.search(message.content):
                cursor_hello.execute(
                    "SELECT response_text FROM greetings_table ORDER BY RANDOM() LIMIT 1"
                )
                response = cursor_hello.fetchone()[0]
                await message.reply(response, mention_author=True)


client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))