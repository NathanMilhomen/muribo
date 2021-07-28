from discord.ext import commands

from utils import load_json, load_locale

config = load_json("config.json")
_ = load_locale("project", "locales", [config["language"]])


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
