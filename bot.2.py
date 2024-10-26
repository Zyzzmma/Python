import discord
from discord.ext import commands
from generator_hasel import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def haslo(ctx, pass_lenght=10):
    await ctx.send(gen_pass(pass_lenght))
@bot.command()
async def mem(ctx):
    with open("img\mem1.jpeg", "img\mem2.jpeg", 'rb') as file:
        discord_file = discord.File(file)
        await ctx.send(file=discord_file)
bot.run("")
