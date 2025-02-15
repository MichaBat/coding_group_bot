#!/usr/bin/env python3
import disnake
from disnake.ext import commands
from clients.custom_bot_client import CustomBotClient
from config import TOKEN, PREFIX
import asyncio

async def main():
    
    command_sync_flags = commands.CommandSyncFlags.default()
    command_sync_flags.sync_commands_debug = True
    
    intents = disnake.Intents.all()

    bot = CustomBotClient(
        command_prefix=PREFIX,
        intents=intents,
        command_sync_flags=command_sync_flags,
    )
    
    tasks = [
        asyncio.create_task(bot.load_extension('cogs.command_err_handler')),
        asyncio.create_task(bot.load_extension("cogs.messages.hello_world")),
        asyncio.create_task(bot.load_extension("cogs.channel_management.empty_text_channel")),
        asyncio.create_task(bot.load_extension("cogs.roles.role_sender")),
        asyncio.create_task(bot.load_extension("cogs.roles.role_handler")),

    ]
    
    await asyncio.gather(*tasks)
    
    
    try:  
        await bot.start(TOKEN)
    finally:
        await bot.close()
        print("bot closed")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting gracefully...")

