import youtube_dl



def search_youtube(query):
    ytdl = youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'noplaylist': True})
    info = ytdl.extract_info(f"ytsearch:{query}", download=False)
    
    return info['entries'][0]['url']