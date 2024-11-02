# DiscoPy Bot
<img 
    src="./assets/logo.png" 
    alt="logo" 
    width="300px" 
    align="right"
/>


<div align="left">
DiscoPy is a Discord music bot built with Python and the discord.py library. It provides simple commands to play music and YouTube playlists directly in voice channels on your Discord server.

<br>

<p align="center"> 
    <a href="#prerequisites">Prerequisites</a> |
    <a href="#local-installation">Local Installation</a> |
    <a href="#configuration">Configuration</a> |
    <a href="#commands">Commands</a> |
    <a href="#license">License</a> 
</p>

## Prerequisites
- **[Docker](https://docs.docker.com/engine/install/):** 27.1.2
- **[Docker Compose](https://docs.docker.com/compose/install/linux/)**
- **[Python3](https://www.python.org/downloads/):** 3.11.2

## Local Installation
1. **Clone the Repository:**
```bash
git clone https://github.com/Ismael-Moreira-Kt/DiscoPy
cd DiscoPy
```

2. **Create a .env file:**
```env
DISCORD_TOKEN=[the-token-of-the-discord]
VOICE_CHANNEL_ID=[voice-channel-id]
TEXT_CHANNEL_ID=[text-channel-id]
```

You can get a token [here](https://discord.com/developers/docs/intro).

You can get channel_id by right-clicking on the desired chat.

3. **Build the Docker Image:**
```bash
docker compose build
```

4. **Start the Bot with Docker Compose:**
```bash
docker-compose up
```

## Configuration
1. Add the Bot to Your Server:
    - Go to the [Discord Developer Portal](https://discord.com/developers/docs/intro).
    - Generate an invite URL with permissions to connect and speak in voice channels.
    - Add the bot to your Discord server.
2. Required permissions:
    - **Text permissions:**
        - Send Messages
        - Read Messages
        - Send Messages from Embeds
        - Attach Files
        - Add Reactions

    - **Voice permissions:**
        - Connecting to Voice Channels
        - Speaking on Voice Channels

## Commands
- **!play (nome ou URL):** Play a song. It can be a name or a YouTube URL.
- **!playlist (URL):** Plays all the songs in a YouTube playlist.
- **!stop:** Stops the current song and disconnects the bot from the voice channel.
- **!info:** Displays a list of available commands and how to use them.
- **!volume (number):** Adjusts the volume of the song being played. The value must be between 0 and 100.
- **!pause:** Pause the current song.
- **!resume:** Resumes playback of the paused song.
- **!skip:** Skip the current song and move on to the next one in the playlist.
- **!current:** Shows the name of the song currently playing.

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](./LICENSE) file for details.

</div>
