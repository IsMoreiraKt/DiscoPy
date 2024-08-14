import discord
from discord.ext import commands
import youtube_dl
from utils.youtube import search_youtube, get_playlist
import asyncio



ytdl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
}



class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def play(self, ctx, *, query: str):
        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        if 'http' in query:
            url = query
            await self.play_url(ctx, voice_client, url)
        else:
            url = search_youtube(query)
            await self.play_url(ctx, voice_client, url)