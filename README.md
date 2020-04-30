SimpleNotes Discord Bot
=======================

A bot that allows anyone on a server to write simple text notes for anyone to read.  
This was inspired by Telegram bots that I often see on some channels of which I’m a member.


## Requirements

* [Python 3](https://www.python.org) (tested on 3.7.7)
* [Discord.py](https://github.com/Rapptz/discord.py) (tested on 1.3.3)


## Instructions

* Create a `discord_token.txt` file at the project’s root containing the bot’s token
* Execute [`main.py`](main.py): `python3 main.py`


## Usage

```
This is a simple bot to take notes, here are the available commands:

* !help                       - shows this help message
* !notes                      - show a list of all notes available to read
* !note <name>                - read note <name>
* !writenote <name> <content> - write <content> to note <name>, replacing the current content if the note already exists
* !deletenote <name>          - delete note <name>

Made with ❤️ by GilDev! (https://gildev.dev/projets/simplenotesdiscordbot)
```


## TODO

* Logs should be shown through the `logging` package.
* Maybe the `!notes` command could send an embed instead of a flat text, with links on each note name to quickly read one by clicking on its name.