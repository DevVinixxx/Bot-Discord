import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
       return

    if "palavrão" in message.content:
        await message.channel.send(f"Por favor, {message.author.name}, não ofenda os membros")

        await message.delete()

    await bot.process_commands(message)

# !oi
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)

@bot.command(name="criador")
async def send_dev(ctx):
    name = ctx.author.name

    response = "Olá, meu criador é o V N X #6912"

    await ctx.send(response)


@bot.command(name="info")
async def info(ctx):
    name = ctx.author.name

    response = "Olá " + name + ", eu ainda estou em desenvolvimento por enquanto não tenho muitos comandos :P  mas os comandos que tenho são: !oi , !criador e !info. Em breve estarei com muito mais funções legais para entretenimento "

    await ctx.send(response)

#calcular 

@bot.command(name="calcular")
async def calculate(ctx, expression):
    eval()

bot.run("MTA5MzU4MjE2NzU1NDEzNDA2OQ.GBJm0C.4vFfRguSb6Hwfuh2DOhl6PbGa4gjScOc9cdQlY")