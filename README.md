# dtp-bot

DevTown's discord bot

## Installation

### As Docker image

This is the easiest way to get DTP-Bot working.

1. Pull a DTP-Bot image from the [Docker Hub](https://hub.docker.com/r/karmekk/dtp-bot/tags). For example, to pull version 1.1.0:

```
docker pull karmekk/dtp-bot:1.1.0
```

2. Save the [template .env file](https://raw.githubusercontent.com/karmek-k/dtp-bot/master/.env.template), rename it and modify to your needs.

3. Run the image.

```
docker run -d --env-file <PATH TO THE .env FILE> <PULLED IMAGE NAME>
```

For example, if the .env file was saved to `~/.env` and the pulled image name is `karmekk/dtp-bot:1.1.0`:

```
docker run -d --env-file ~/.env karmekk/dtp-bot:1.1.0
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
