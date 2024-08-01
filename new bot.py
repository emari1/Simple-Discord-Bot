import discord
import requests

from discord.ext import commands,tasks

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("hello chat")
    try:
        synced = await client.tree.sync()
        print(f'synced {len(synced)} commands')
    except Exception as e:
        print(e)


@client.tree.command(name='data', description='insert crypto token ID to get price back')
async def data(interaction: discord.Interaction, token_id: str):

    token_id=token_id.lower().lstrip().rstrip().replace(' ','-')
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-Qw9Boe64i5XXXXXXXXX"
    }
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        value = data['market_data']['current_price']['usd']
        name=data['localization']['en']
        await interaction.response.send_message(f'the current value of {name} is ${value} USD')
    except Exception as e:
        await interaction.response.send_message(e)




client.run('xxxx')


