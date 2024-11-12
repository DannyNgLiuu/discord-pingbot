import discord
import os
from dotenv import load_dotenv

#grabs the discord token
load_dotenv()

#allows for the bot to read messages
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    #prevents infinite pings
    if message.author == client.user:
        return

    if message.channel.id == 1302887472975319040:
        role_mention = "<@&1302883621190893630>"
        await message.channel.send(f"{role_mention}")

if __name__ == "__main__":
    client.run(os.getenv("DISCORD_TOKEN"))
