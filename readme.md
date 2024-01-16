# Discord Nickname Changer Bot

## Overview
This is a simple Discord bot written in Python using the Discord.py library. The purpose of this bot is to change the nicknames of all members in a specified guild to randomly selected names from a file.

## Features
- Changes nicknames of all members in the specified guild.
- Nicknames are randomly selected from a list of names in a file.

## Prerequisites
- Python 3.x
- discord.py library (install using `pip install discord.py`)

## Setup
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a Discord bot and obtain its token.
4. Create a `config.json` file inside the `settings` folder with the following structure:
    ```json
    {
      "token": "YOUR_BOT_TOKEN",
      "guild_id": 1232 <= must be an int
    }
    ```
5. Create a `names.txt` file inside the `src` folder with a list of names, each on a separate line.

## Usage
1. Run the bot using `python bot.py` in the terminal.
2. The bot will log in and change the nicknames of all members in the specified guild.
3. The bot will print each member's new nickname to the console.

## Configuration
You can customize the bot's behavior by modifying the `config.json` file. Adjust the `token` and `guild_id` values to match your Discord bot's token and the ID of the guild you want to operate on.

## Disclaimer
This bot is a simple demonstration and may not cover all edge cases. Use it responsibly and be aware of Discord's Terms of Service.

Feel free to contribute, report issues, or suggest improvements!
