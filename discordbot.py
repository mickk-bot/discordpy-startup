from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
    
@bot.command()
async def おはよう(ctx):
    await ctx.send("おはようございます" + ctx.author.name + "さん！") 
    
@bot.command()
async def こんにちは(ctx):
    await ctx.send("こんにちは" + ctx.author.name + "さん！")
    
@bot.command()
async def おやすみ(ctx):
    await ctx.send("おやすみ" + ctx.author.name + "さん！")
    
@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)
    

bot.run(token)
