import discord
import asyncio
from discord.ext import commands

def run_selfbot(token, spam_message, spam_amount, spam_delay):
    intents = discord.Intents.default()
    intents.messages = True
    bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

    @bot.event
    async def on_ready():
        print(f"✅ Logged in as {bot.user}")
        for guild in bot.guilds:
            for channel in guild.text_channels:
                try:
                    for _ in range(spam_amount):
                        await channel.send(spam_message)
                        await asyncio.sleep(spam_delay)
                except:
                    continue

    bot.run(token, bot=False)
