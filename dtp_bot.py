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
    # (I wrapped the filter object in a list
    # so that it can be accessed more than once)
    roles = list(
        filter(lambda role: role.name in args, allowed_roles)
    )

    if roles:
        await user.add_roles(*roles)
        await ctx.send(
            f'Roles {", ".join(map(str, roles))} have been given to {user.name}.'
        )
    else:
        await ctx.send(f'No roles were given to {user.name}.')


@bot.command()
async def role_remove(ctx, *args):
    """
    Removes roles from a user.
    :param ctx: context
    :param args: role names
    """
    user = ctx.message.author
    user_roles = user.roles
    roles_to_remove = list(
        filter(
            lambda role: role.name in args
                         and str(role.color) == CONSTANTS['ALLOWED_ROLE_COLOR'],
            user_roles
        )
    )

    if roles_to_remove:
        await user.remove_roles(*roles_to_remove)
        await ctx.send(f'Successfully removed roles {", ".join(args)}.')
    else:
        await ctx.send(f'No roles were removed from {user.name}.')


@bot.command()
async def role_clear(ctx):
    """
    Removes all roles from a user.
    :param ctx: context
    """
    user_role_names = tuple(map(str, ctx.message.author.roles))
    await role_remove(ctx, *user_role_names)


# Messages
print('Starting the bot...\nConstants:')
for k, v in CONSTANTS.items():
    print(f'{k}: {v}')

bot.run(os.getenv('BOT_TOKEN'))
