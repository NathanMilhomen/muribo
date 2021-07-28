from discord.ext import commands
from random import randint
from asyncio import sleep


class Flood(commands.Cog, name="flood"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="flood")
    async def flood(self, context, *, message):
        """
        Floods a message
        """
        for _ in range(randint(5, 10)):
            await context.message.channel.send(message)
            await sleep(1)


def setup(bot):
    bot.add_cog(Flood(bot))
