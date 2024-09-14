import discord
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Pasa tutorial de como dormir'):
        await message.channel.send("https://youtu.be/1wvL99nmIUU?si=o2u4qSYdbf4FKMyF")
    elif message.content.startswith('Pikachu'):
        await message.channel.send("https://pbs.twimg.com/media/D8Sx5FnXoAAXolQ?format=jpg&name=240x240")
    elif message.content.startswith('Genera una contraseña:'):
        await message.channel.send(f"Contraseña: {gen_pass(8)}")
    elif message.content.startswith('Tienda de regalos go'):
        await message.channel.send("https://store.pokemongolive.com/es-ES/offer-redemption")
    elif message.content.startswith('Pagina python'):
       await message.channel.send("https://learn.kodland.org/my-courses/1218/at-class")
    elif message.content.startswith('Github'):
       await message.channel.send("https://github.com/")
    else:
        await message.channel.send(message.content)

client.run("MTI4NDI5ODMzNDgwMjI4MDQ3Mw.G0030N.Lm0PXB0obguaBnY0gKgMhwc5kdv3WeZEthTXDU")
