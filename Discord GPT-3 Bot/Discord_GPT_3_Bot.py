# Discord bot integrated with GPT API
import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv('OPENAI_KEY')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_message(message):
# Only respond to messages from other users, not from the bot
    if message.author == client.user:
        return
    
    # Only respond if @mentioned bot, check if the bot is mentioned in message
    if client.user in message.mentions:
        # Use the OpenAI API to generate a response to the message
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.content}",
        max_tokens=4000,
        temperature=0.7,
        )
        
        # Send the response as a message
        await message.channel.send(response.choices[0].text)

# start the bot
client.run(TOKEN)