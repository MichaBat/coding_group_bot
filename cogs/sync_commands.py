import disnake
from disnake.ext import commands

class CommandReloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload_commands", description="Reload the bot's slash commands.")
    async def reload_commands(self, ctx):
        """Reload the Slash commands and sync them with Discord."""
        try:
            # Sync the commands with Discord again
            await self.bot.tree.sync()
            await ctx.send("Slash commands have been reloaded and synced!")
        except Exception as e:
            await ctx.send(f"An error occurred while reloading commands: {str(e)}")

def setup(bot):
    bot.add_cog(CommandReloader(bot))
