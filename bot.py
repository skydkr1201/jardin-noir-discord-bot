import discord
from discord.ext import commands
import random
from gages import GAGES_SEXY, GAGES_MEURTRE, GAGES_MIXTES
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def gage(ctx):
    gage_type = random.choice(["SEXY", "MEURTRE", "MIXTE"])
    if gage_type == "SEXY":
        gage = random.choice(GAGES_SEXY)
    elif gage_type == "MEURTRE":
        gage = random.choice(GAGES_MEURTRE)
    else:
        gage = random.choice(GAGES_MIXTES)
    await ctx.send(f"**Gage {gage_type}** : {gage}")

@bot.command()
async def helpgage(ctx):
    await ctx.send("Commandes disponibles : `!gage`, `!helpgage`")

bot.run(os.getenv("DISCORD_TOKEN"))