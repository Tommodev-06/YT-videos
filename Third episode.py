from diskord.ext import commands, tasks

client=commands.Bot(command_prefix="t!")

@client.event
async def on_ready():
    print(f"{client.user} is online")

@tasks.loop(seconds=2)
async def spam():
    channel=client.get_channel(channel-id) # the ID is an int, not a str
    await channel.send("Spam message")

@client.command(help="Command to start the spam task")
async def startspam(ctx):
    spam.start()
    await ctx.send("The spam task has been started")

@client.command(help="Command to stop the spam task")
async def stopspam(ctx):
    spam.stop()
    await ctx.send("The spam task has been stopped")

client.run("bot-token")
