import discord
from discord.ext import commands
import importlib
import logging
import os
import random

from Notes import Notes
from helpers import getPath

logging.basicConfig(level=logging.INFO)
with open("discord_token.txt", "r") as f:
    token = f.readline().rstrip()

bot = commands.Bot(command_prefix='!')

# TODO: Add `!help` command or comment code properly to use the default one
# "This is a simple bot to take notes, here are the available commands:\n"
# "* `!help`: shows this help message\n"
# "\n"
# "* `!notes`: show a list of all notes available to read\n"
# "* `!note <name>: read note “<name>”\n"
# "* `!writenote <name> <content>`: write <content> to note “name”, replacing the current context if the note already exists\n"
# "* `!deletenote <name>`: delete note <name>\n"
# "\n"
# "Made with love by [GilDev](https://gildev.dev)"


@bot.event
async def on_ready():
    print(f"Connected as {bot.user}!")


@bot.command()
async def notes(ctx):
    """Shows a list of all notes available to read"""
    # TODO: Make this an embed so commands to read each note can be embedded in
    #       notes names

    notes = Notes(getPath(ctx)).getAll()
    if notes:
        message = "Here are the notes available to read:\n\n"
        for name in notes.keys():
            message += f"* {name}\n"

        message += "\nUse `!note <name>` to read a note!"
    else:
        message = "There are no notes! You can add one with `!writenote <name> <content>`."

    await ctx.send(message)

# TODO: multiple aliases for this command (readnote, getnote)
@bot.command()
async def note(ctx, name):
    """Read a note"""

    name = name.lower().replace(" ", "-")
    content = Notes(getPath(ctx)).get(name)
    if content:
        message = content
    else:
        message = f"Note “{name}” does not exist.\nUse `!notes` to get a list of available notes."

    await ctx.send(message)


@note.error
async def note_error(ctx, error):
    await ctx.send("Usage: `!note <name>`\nUse `!notes` to get a list of available notes.")

# TODO: multiple aliases for this command (addnote, createnote, newnote?)
@bot.command()
async def writenote(ctx, *, args):
    try:
        (name, content) = args.split(maxsplit=1)
    except ValueError:
        await ctx.send("You must provide a content for the note.\nUsage: `!writenote <name> <content>`")
        return

    name = name.lower().replace(" ", "-")
    content = content.strip()
    if len(name) > 30:
        await ctx.send("Note name cannot exceed 30 characters.")
        return

    # Write notes to file
    notes = Notes(getPath(ctx))
    notes.write(name, content)
    print(
        f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")

    await ctx.send(f"Successfully wrote note “{name}”, use `!note {name}` to read it!")


@writenote.error
async def writenote_error(ctx, error):
    print(f"Error on !writenote: {error}")
    await ctx.send("Usage: `!writenote <name> <content>`")


@bot.command()
async def deletenote(ctx, name):
    name = name.lower().replace(" ", "-")
    notes = Notes(getPath(ctx))

    if notes.delete(name):
        message = f"Note “{name}” successfully deleted!"
        print(
            f"Deleted note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id})")
    else:
        message = f"Note {name} does not exist.\nUse `!notes to get a list of available notes."

    await ctx.send(message)


@deletenote.error
async def deletenote_error(ctx, error):
    print(f"Error on !deletenote: {error}")
    await ctx.send("Usage: `!deletenote <name>`\nUse `!notes` to get a list of available notes.")

bot.run(token)
