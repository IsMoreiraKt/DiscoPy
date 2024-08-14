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

    async def play_url(self, ctx, voice_client, url):
        ytdl = youtube_dl.YoutubeDL(ytdl_opts)
        info = ytdl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

        ffmpeg_opts = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn',
        }

        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(url2, **ffmpeg_opts))

        await ctx.send(f"Now playing: {info['title']}")


    @commands.command()
    async def playlist(self, ctx, *, url: str):
        if ctx.author.voice is None:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        if 'playlist' in url:
            urls = get_playlist(url)
            await self.play_playlist(ctx, voice_client, urls)
        else:
            await ctx.send("The provided URL is not a valid playlist.")