# Basic slash command
import diskord
from diskord.ext import commands

client=commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print(f"{client.user} is online")

@client.slash_command(description="First slash command", guild_ids=[your-guild-id]) # the ID is an int, not a str
async def test(ctx):
    await ctx.send("Slash commands eheh")

client.run("bot-token")

# Slash command with option

import diskord
from diskord.ext import commands

client=commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print(f"{client.user} is online")

@client.slash_command(description="First slash command", guild_ids=[your-guild-id]) # the ID is an int. not a str
@diskord.application.option("message", description="Message to send")
async def test(ctx, *, message: str):
    await ctx.send(f"Message: ```{message}```")

client.run("bot-token")
