import disnake
from disnake.ext import commands

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Replies with Hello, world!"""
        await ctx.send("Hello, world!")

def setup(bot):
    bot.add_cog(HelloWorld(bot))
