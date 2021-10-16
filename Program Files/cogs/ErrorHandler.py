import inspect
import discord
import asyncio
import random
import json
import traceback
import datetime
import asyncpg
import sys
from discord import user
from discord import integrations
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        emote = json.load(open('Program Files\Emotes.json'))    
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        notfound    =   (commands.CommandNotFound, )
        error   =   getattr(error, 'original', error)
        mu  =   [f'{emote["frog"]["worry"]}',
                f'{emote["frog"]["hmm"]}',
                f'{emote["frog"]["worryrun"]}',
                f'{emote["panda"]["think"]}',
                f'{emote["sed"]["cet"]}',
                f'{emote["peep"]["sadsip"]}',
                f'{emote["random_themed"]["pokikill"]}',
                f'{emote["panda"]["snap"]}',
                f'{emote["anxiety"]["sus"]}',
                f'{emote["anxiety"]["triggered"]}',
                f'{emote["anxiety"]["shit"]}']
        color = discord.Color.from_rgb(117, 128, 219)

        if isinstance(error, notfound):
            return
        
        if isinstance(error, commands.DisabledCommand):
            emb = discord.Embed(
                title = 'OOP -',
                color = color)
            emb.add_field(
                name = f'__***Command: {ctx.command}***__',
                value = f'```py\n{error}\n```')
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.reply(embed = emb)
    
        if  isinstance(error, commands.BotMissingPermissions):
            emb = discord.Embed(
                title = 'Thats Depressing -',
                color = color)
            emb.add_field(
                name = f'__***Missing Perms : {ctx.command}***__',
                value = f'```py\n{error}\n```')
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.reply(embed = emb)

        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(
                title = 'OOPS!',
                color = color)
            emb.add_field(
                name = f'__***Missing Perms : {ctx.command}***__  {random.choice(mu)}',
                value = f'```py\n{error} \n```\n')
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            async with ctx.typing():
                await asyncio.sleep(0.5)
            await ctx.reply(embed = emb)

        if isinstance(error, commands.NotOwner):
            emb = discord.Embed(
                title = 'Suck on That',
                color = color)
            emb.add_field(
                name = f'__***Command: {ctx.command}***__ {random.choice(mu)}',
                value = f'```py\n {error}\n```')
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            await ctx.reply(embed = emb)
        
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(
                title = 'Yikes !',
                color = color)
            emb.add_field(
                name = f'__***Args Missing : {ctx.command}***__ {random.choice(mu)}',
                value = f'```pi\n {error}\n```')
            emb.timestamp = datetime.datetime.now(datetime.timezone.utc)

        else:
            errorsend = 894957830375899157
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            channel = self.bot.get_channel(errorsend)
            emb = discord.Embed(
                title = 'Errors going BOING!',
                color = color)
            emb.add_field(
                name = f'__***{error}***__',
                value = f'{ctx.author.mention} did this in <#{ctx.channel.id}> in `{ctx.guild.name}`\n```py\n{traceback}\n{traceback.format_exception}\n```')
            emb.timestamp = emb.timestamp = datetime.datetime.now(datetime.timezone.utc)
            await channel.send(embed = emb)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
