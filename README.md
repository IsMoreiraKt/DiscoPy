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
- **!play (nome ou URL):** Toca uma música. Pode ser um nome ou uma URL do YouTube.
- **!playlist (URL):** Toca todas as músicas de uma playlist do YouTube.
- **!stop:** Para a música atual e desconecta o bot do canal de voz.
- **!info:** Exibe uma lista de comandos disponíveis e como usá-los.
- **!volume (número):** Ajusta o volume da música em reprodução. O valor deve estar entre 0 e 100.
- **!pause:** Pausa a música atual.
- **!resume:** Retoma a reprodução da música pausada.
- **!skip:** Pula a música atual e passa para a próxima na lista de reprodução.
- **!current:** Mostra o nome da música que está tocando atualmente.

## License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](./LICENSE) file for details.

</div>