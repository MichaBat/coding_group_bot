import disnake
from disnake.ext import commands

from .role_handler import RoleButton  # Import RoleButton

class RoleSender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def send_role_message(self, ctx):
        """Send a message with role selection buttons, then unload itself."""
        roles = [
            "Beginner",
            "Intermediate",
            "Advanced",
            "Front-end",
            "Back-end",
            "Mobile Dev",
            "AI / ML",
            "Game Dev",
            "DevOps"
        ]
        
        embed = disnake.Embed(title="Select Your Role", description="Click a button below to get or remove a role.", color=disnake.Color.blue())
        await ctx.send(embed=embed, view=RoleButton(roles))

        # Unload the cog after sending
        cog_name = "cogs.roles.role_sender"
        await self.bot.unload_extension(cog_name)
        print(f"Unloaded {cog_name} after sending role message.")

def setup(bot):
    bot.add_cog(RoleSender(bot))
