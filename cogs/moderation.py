import discord
from discord.ext import commands

from utils.utils import _


class Moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason=_("Not specified")):
        _(
            """
        Kick a user out of the server.
        """
        )
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title=_("Error!"),
                description=_("User has Admin permissions."),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        else:
            try:
                await member.kick(reason=reason)
                embed = discord.Embed(
                    title=_("User Kicked!"),
                    description=_(
                        f"**{member.nick}** was kicked by **{context.message.author.nick}**!"
                    ),
                    color=0x42F56C,
                )
                embed.add_field(name=_("Reason:"), value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        _(
                            f"You were kicked by **{context.message.author.nick}**!\nReason: {reason}"
                        )
                    )
                except:
                    pass
            except:
                embed = discord.Embed(
                    title=_("Error!"),
                    description=_(
                        "An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick."
                    ),
                    color=0xE02B2B,
                )
                await context.message.channel.send(embed=embed)

    @commands.command(name="nick")
    async def nick(self, context, member: discord.Member, *, nickname=None):
        _(
            """
        Change the nickname of a user on a server.
        """
        )
        try:
            await member.edit(nick=nickname)
            embed = discord.Embed(
                title=_("Changed Nickname!"),
                description=_(
                    "**{member.nick}'s** new nickname is **{nickname}**!"
                ).format(member=member, nickname=nickname),
                color=0x42F56C,
            )
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                title=_("Error!"),
                description=_(
                    "An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname."
                ),
                color=0xE02B2B,
            )
            await context.message.channel.send(embed=embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason="Not specified"):
        _(
            """
        Bans a user from the server.
        """
        )
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title=_("Error!"),
                    description=_("User has Admin permissions."),
                    color=0xE02B2B,
                )
                await context.send(embed=embed)
            else:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title=_("User Banned!"),
                    description=_(
                        f"**{member.nick}** was banned by **{context.message.author.nick}**!"
                    ),
                    color=0x42F56C,
                )
                embed.add_field(name=_("Reason:"), value=reason)
                await context.send(embed=embed)
                await member.send(
                    _(
                        f"You were banned by **{context.message.author.nick}**!\nReason: {reason}"
                    )
                )
        except:
            embed = discord.Embed(
                title=_("Error!"),
                description=_(
                    "An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban."
                ),
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @commands.command(name="warn")
    async def warn(self, context, member: discord.Member, *, reason=_("Not specified")):
        _(
            """
        Warns a user in his private messages.
        """
        )
        embed = discord.Embed(
            title=_("User Warned!"),
            description=_(
                f"**{member.nick}** was warned by **{context.message.author.nick}**!"
            ),
            color=0x42F56C,
        )
        embed.add_field(name=_("Reason:"), value=reason)
        await context.send(embed=embed)
        try:
            await member.send(
                _(
                    f"You were warned by **{context.message.author.nick}**!\nReason: {reason}"
                )
            )
        except:
            pass

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def purge(self, context, amount):
        _(
            """
        Delete a number of messages.
        """
        )
        try:
            amount = int(amount)
        except:
            embed = discord.Embed(
                title=_("Error!"),
                description=_(f"`{amount}` is not a valid number."),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
            return
        if amount < 1 or amount > 1000:
            embed = discord.Embed(
                title=_("Error!"),
                description=_(f"`{amount}` is not a valid number."),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
            return
        purged_messages = await context.message.channel.purge(limit=amount)
        embed = discord.Embed(
            title=_("Chat Cleared!"),
            description=_(
                f"**{context.message.author.nick}** cleared **{len(purged_messages)}** messages!"
            ),
            color=0x42F56C,
        )
        await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
