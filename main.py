import os
import openai
import discord 
from discord.ext import commands
from discord import app_commands
import asyncio 
import tracemalloc
from dotenv import load_dotenv
import sys
import time
import subprocess



load_dotenv()
discord_token = os.getenv("TOKEN")
openaikey = os.getenv("key")

channel1 = os.getenv("channel1")
channel2 = os.getenv("channel2")
channel3 = os.getenv("channel3")

channel11 = int(channel1) #This is the 
channel22 = int(channel2) #Best i can 
channel33 = int(channel3) #Come up with :skull:



openai.api_key = (openaikey)

#1

client = commands.Bot(command_prefix="!", intents=discord.Intents.all(),case_insensitive=True)


with open('F:\Python\SakuraNeNaiFinal\content1.txt', 'r',encoding='utf-8') as file:
    content = file.read()

conversations = {}



@client.event
async def on_message(message: discord.Message):
    user = message.author.id
    channel = message.channel.id

    if user in conversations and channel == 1089017484662800474 or channel == 1041060610726711316:
        conversation = conversations[user]
        if len(conversation) >= 15:
           del conversations[user]
        else:
            conversation.append({"role": "user", "content": message.content})
        
        messages = [
        {"role": "system", "content": conversation[i]["content"]} for i in range(len(conversation))       
        ]
        messages.append({"role": "system", "content": content})
        messages.append({"role": "assistant", "content": "your name is sakura"})
        messages.append({"role": "user", "content": message.content})
    else:
        conversation = []
        messages = [
            {"role": "system", "content": content},
            {"role": "assistant", "content": "your name is sakura"},
            {"role": "user", "content": message.content}
        ]


    try:
        h2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=1000,
            messages=messages
        )
        h3 = h2['choices'][0]['message']['content']
        h4 = h3.split('DAN: ')
    except Exception as e:
        await message.channel.send(f"Sorry, an error occurred: {e}. Please try again later.(tldr: It crashed)")
        return

    if message.content.startswith('!restart'):
        await message.channel.send('Restarting...')
        python = sys.executable
        os.execl(python, python, *sys.argv)
    if message.author.bot:
        return
    if channel == channel11 or channel == channel22 or channel == channel33: 
        if message.content.startswith('!clear'):
            del conversations[user]
            await message.channel.send('cleared previous conversations')
        if message.content.startswith('!'):
            return
        try:
            conversations[user] = conversation
            conversation.append({"role": "assistant", "content": h4[1]})
            async with message.channel.typing():
              await asyncio.sleep(2)
              await message.channel.send(h4[1],reference=message)
              print(conversations)
        except IndexError:            
            await message.channel.send("Sorry an Error occured, please try that again|\n",h4[0],reference=message)

            
    else:
        pass
    await asyncio.sleep(200)


client.run(discord_token)
