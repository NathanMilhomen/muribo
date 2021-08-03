from discord.ext import commands

from utils.utils import config, _


class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="testcommand")
    async def testcommand(self, context):
        """
        Documentação
        """

        pass


# Adiciona o comando
# def setup(bot):
#     bot.add_cog(Template(bot))
