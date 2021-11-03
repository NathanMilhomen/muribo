from random import randint, choice
from discord.ext import commands

from utils.utils import config, _


class Random(commands.Cog, name="random"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="random")
    async def random(self, context, *, args=""):
        """
        if args were provided, choose beetwen then, else randomly says a number
        beetween 0, 100
        """

        if not args:
            await context.message.channel.send(randint(0, 100))
        elif len(args.split(" ou ")) > 1:
            await context.message.channel.send(choice(args.split(" ou ")))


def setup(bot):
    bot.add_cog(Random(bot))
