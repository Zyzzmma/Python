import discord
from discord.ext import commands
from generator_hasel import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
eko1 = ["Słoik", "Butelka", "Książka", "Okulary"]
pojemniki = {
    "Słoik": "pojemnika na szkło",
    "Butelka": "pojemnika na plastik lub szkło (w zależności od materiału)",
    "Książka": "pojemnika na papier",
    "Okulary": "specjalnego punktu zbiórki lub pojemnika na szkło"
}
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.event
async def on_message(message):
    # Ignoruje wiadomości wysyłane przez samego bota
    if message.author == bot.user:
        return

    # Sprawdza, czy wiadomość zawiera element z listy eko1
    for item in eko1:
        if item.lower() in message.content.lower():
            odpowiedz = f"{item} należy wyrzucić do {pojemniki[item]}."
            await message.channel.send(odpowiedz)
            break

    # Przekazuje wiadomość dalej do innych komend
    await bot.process_commands(message)


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
    with open("img\mem1.jpeg", 'rb') as file:
        discord_file = discord.File(file)
        await ctx.send(file=discord_file)
@bot.command()
async def ekol(ctx):
    await ctx.send(eko1)
@bot.command()
async def eko(ctx, ekologia):
    await ctx.send(ekologia)

bot.run("")
