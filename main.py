import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

import os
import platform
import random
import sys

from decouple import config as env

from utils.utils import config, _, load_json
from utils import db

intents = discord.Intents.default()

bot = Bot(command_prefix=config["bot_prefix"], intents=intents)


@bot.event
async def on_ready():
    print(_("Logged in as {name}").format(name=bot.user.name))
    print(
        _("Running on: {system} {release} ({os})").format(
            system=platform.system(), release=platform.release(), os=os.name
        )
    )
    print(("-------------------"))


bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(_("Loaded extension '{extension}'").format(extension=extension))
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(
                    _("Failed to load extension {extension}\n{exception}").format(
                        extension=extension, exception=exception
                    )
                )


@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    blacklist = db.execute("SELECT id FROM blacklist;")

    if blacklist and message.author.id in blacklist:
        return
    await bot.process_commands(message)


@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        _(
            f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})"
        )
    )


@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            title=_("Hey, please slow down!"),
            description=_(
                f"You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}."
            ),
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title=_("Error!"),
            description=_("You are missing the permission `")
            + ", ".join(error.missing_perms)
            + _("` to execute this command!"),
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title=_("Error!"),
            description=str(error).capitalize(),
            color=0xE02B2B,
        )
        await context.send(embed=embed)
    raise error


bot.run(env("TOKEN"))
