from bs4 import BeautifulSoup
from discord.ext import commands
import requests
from random import choice
from utils.utils import config, _


class Pic(commands.Cog, name="pic"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pic")
    @commands.cooldown(5, 10)
    async def pic(self, context, *, image):
        """
        Searchs a picture in google and sends here.
        """

        try:
            html = requests.get(
                f"https://www.google.com/search?tbm=isch&q={image}"
            ).text
            soup = BeautifulSoup(html, "html.parser")
            html_images = soup.find_all("img")

            chances = 0
            while chances < 10:
                url = choice(html_images)["src"]
                if not url.endswith(".gif"):
                    await context.send(url)
                    return
                chances += 1

            await context.send("I can't find this image")

        except:
            await context.send("Something got wrong :confused:")


def setup(bot):
    bot.add_cog(Pic(bot))
