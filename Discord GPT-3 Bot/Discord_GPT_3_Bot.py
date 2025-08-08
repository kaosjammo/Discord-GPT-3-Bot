# Discord bot integrated with OpenAI GPT-5 API
import os
import discord
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai_client = OpenAI(api_key=OPENAI_KEY)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    """Respond to messages that mention the bot using OpenAI's GPT-5 model."""
    if message.author == client.user:
        return

    if client.user in message.mentions:
        completion = openai_client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": message.content}],
            max_tokens=4000,
            temperature=0.7,
        )
        reply = completion.choices[0].message["content"]
        await message.channel.send(reply)

# Start the bot
client.run(DISCORD_TOKEN)
