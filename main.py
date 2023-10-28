import discord
import requests
import json
import meraopenai
intents = discord.Intents.all()
client = discord.Client(intents=intents)


def get_answer(prompt):
    prompt = prompt[2:]
    return meraopenai.ask(prompt)


@ client.event
async def on_ready():
    with open('image.jpg', 'rb') as image:
        await client.user.edit(avatar=image.read())
    print("logged in")


@ client.event
async def on_message(message):
    if message.content.startswith("nD"):
        answer = get_answer(message.content)
        if message.author == client.user:
            return
        channel = message.channel
        await message.reply(answer)
client.run(
    "MTA1MTQ4OTE3NDU4NDMwMzY0Nw.G0YaB0.7FPXqgCMpazVXm4zfVRchvzcAuUhDQikTgO--A")
