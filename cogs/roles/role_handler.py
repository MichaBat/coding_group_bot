import disnake
from disnake.ext import commands
from disnake.utils import get

class RoleHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_role_buttons(self, ctx, *roles):
        """Creates a message with role buttons for the provided role names."""
        view = RoleButton(roles)
        await ctx.send("Choose your roles:", view=view)

class RoleButton(disnake.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=None)
        self.roles = roles
        
        for role_name in roles:
            self.add_item(RoleButtonButton(role_name))

class RoleButtonButton(disnake.ui.Button):
    def __init__(self, role_name):
        super().__init__(label=role_name, style=disnake.ButtonStyle.primary)
        self.role_name = role_name
    
    async def callback(self, interaction: disnake.Interaction):
        guild = interaction.guild  # Corrected this line
        member = interaction.user
        role = get(guild.roles, name=self.role_name)
        
        if not role:
            await interaction.response.send_message(f"Role `{self.role_name}` not found.", ephemeral=True)
            return
        
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message(f"Removed `{self.role_name}` role.", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message(f"Added `{self.role_name}` role.", ephemeral=True)

def setup(bot):
    bot.add_cog(RoleHandler(bot))
