import diskord
from diskord.ext import commands

client=commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print(f"{client.user} is online")

@client.command(help="Test command")
async def test(ctx):
    await ctx.send("Test command with diskord library")

client.run("bot-token")
