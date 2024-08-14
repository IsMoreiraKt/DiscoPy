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

    async def play_playlist(self, ctx, voice_client, urls):
        for url in urls:
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
            
            while voice_client.is_playing():
                await asyncio.sleep(1)


    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("I am not in a voice channel.")
            return

        await ctx.voice_client.disconnect()
        await ctx.send("Stopped and disconnected.")


    @commands.command()
    async def info(self, ctx):
        info_message = (
            "**Music Bot Commands**\n"
            "`!play <name or URL>`: Play a single song from YouTube. If a name is provided, it will search for the song. If a URL is provided, it will play the song directly.\n"
            "`!playlist <playlist URL>`: Play all songs in a YouTube playlist.\n"
            "`!stop`: Stop the current song and disconnect from the voice channel.\n"
            "`!info`: Show information about how to use the bot.\n"
        )
        
        await ctx.send(info_message)