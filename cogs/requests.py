import requests
import json

from discord.ext import commands

from utils.utils import config, _
from decouple import config as env


class Requests(commands.Cog, name="mir4"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="draco")
    async def draco(self, context, *, flag=""):
        """
        Gets realtime DRACO's price
        """
        request = requests.post(env("DRACO_URL"))

        latest_price = json.loads(request.text)
        draco_usd = float(latest_price["Data"]["USDDracoRate"])

        flag = flag.upper()
        if flag == ("BRL"):
            draco_brl = await self.dolar() * draco_usd
            await context.message.channel.send(
                f"Valor do draco é: R${round(draco_brl, 2)}"
            )
        else:
            await context.message.channel.send(
                f"Draco's value is: ${round(draco_usd, 2)}"
            )

    async def dolar(self):
        "Gets dolar's price"

        request = requests.get(env("DOLAR_URL"))
        latest_price = json.loads(request.text)

        usd = float(latest_price["USDBRL"]["ask"])

        return usd


def setup(bot):
    bot.add_cog(Requests(bot))
