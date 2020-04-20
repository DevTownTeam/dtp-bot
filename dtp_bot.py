#!/usr/bin/env python3

import os
import logging

from discord.ext import commands
from dotenv import load_dotenv

# Enable logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

# Load environment variables
load_dotenv()

# Constants
CONSTANTS = {
    'ALLOWED_ROLE_COLOR': '#' + os.getenv("ALLOWED_ROLE_COLOR"),
    'BOT_TOKEN_PRESENT': bool(os.getenv('BOT_TOKEN'))
}

# Create a Bot instance
bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'))


@bot.command()
async def role_add(ctx, *args):
    """
    Gives roles to the player who invoked the command.
    :param ctx: context
    :param args: role names
    """
    # Aliases
    user = ctx.message.author
    allowed_roles = filter(
        lambda role: str(role.color) == CONSTANTS['ALLOWED_ROLE_COLOR'],
        ctx.guild.roles
    )

    # Roles
    # (I wrapped them in lists so that they can be accessed
    # more than once)
    requested_role_names = list(map(lambda s: s.lower(), args))
    roles = list(
        filter(
            lambda role: role.name in requested_role_names,
            allowed_roles
        )
    )

    if roles:
        await user.add_roles(*roles)
        await ctx.send(
            f'Roles {", ".join(map(str, roles))} have been given to {user.name}.'
        )
    else:
        await ctx.send(f'No roles have been given to {user.name}.')

# Messages
print('Starting the bot...\nConstants:')
for k, v in CONSTANTS.items():
    print(f'{k}: {v}')

bot.run(os.getenv('BOT_TOKEN'))
