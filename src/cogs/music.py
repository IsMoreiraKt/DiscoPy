import discord
from discord.ext import commands
import youtube_dl
from utils.youtube import search_youtube, get_playlist
import asyncio



ytdl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
}