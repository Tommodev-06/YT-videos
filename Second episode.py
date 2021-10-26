import diskord
from diskord.ext import commands

client=commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print(f"{client.user} is online")

@client.slash_command(description="First slash command", guild_ids=[866626689625882624])
@diskord.application.option("message", description="Message to send")
async def test(ctx, *, message: str):
    await ctx.send(f"Message: ```{message}```")

client.run("bot-token")
