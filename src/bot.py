import discord
from discord.ext import commands
from dotenv import load_dotenv
import os



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.load_extension('cogs.music')
