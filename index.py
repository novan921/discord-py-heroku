import os
from discord.ext import commands

BOT_PREFIX = ("?")
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(TOKEN)