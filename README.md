# dtp-bot

DevTown's discord bot

## Installation

### As Docker image

This is the easiest way to get DTP-Bot working.

1. Pull a DTP-Bot image from the [Docker Hub](https://hub.docker.com/r/karmekk/dtp-bot):

```
docker pull karmekk/dtp-bot
```

2. Save the [template .env file](https://raw.githubusercontent.com/karmek-k/dtp-bot/master/.env.template), rename it and modify to your needs.

3. Run the image.

```
docker run -d --env-file <PATH TO THE .env FILE> karmekk/dtp-bot
```

For example, if the .env file was saved to `~/.env`:

```
docker run -d --env-file ~/.env karmekk/dtp-bot
```

## Commands

_I assume that the default command prefix was not changed_

Adding / removing roles:

```
-role_add <role1> [role2] [role3] [...]
-role_remove <role1> [role2] [role3] [...]
-role_clear
```

Warning a user:

```
-warn <user> [reason]
```
