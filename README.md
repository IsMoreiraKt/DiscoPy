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
https://github.com/Ismael-Moreira-Kt/DiscoPy
cd DiscoPy
```

2. **Create a .env file:**
```env
DISCORD_TOKEN=your_discord_bot_token
```

You can get a token [here](https://discord.com/developers/docs/intro).

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
2. Required Permissions:
    - Connect to voice channels
    - Speak in voice channels



</div>