# Package Manager (apt-get)

Grey Hack models software distribution with repositories and an `apt-get`-style client, similar to a real Debian system.

## Repositories

A repository is a server (often a *hackshop*) that hosts installable programs and libraries, usually on port **1542**. Your sources are listed in `/etc/apt/sources.txt`.

## Common commands

| Command | Description |
|---|---|
| `apt-get update` | Refresh the package list from your repositories. |
| `apt-get install <name>` | Install a program or library. |
| `apt-get show` | List available packages. |
| `apt-get search <term>` | Search for a package. |

## Adding a repository

Edit `/etc/apt/sources.txt` to add a repository's IP and port, or use the `aptClient` object in GreyScript:

```greyscript
apt = include_lib("/lib/aptclient.so")
apt.add_repo("1.2.3.4", 1542)
apt.update
apt.install("metaxploit.so")
```

The `aptClient` API includes `add_repo`, `del_repo`, `update`, `install`, `show`, `search`, and `check_upgrade`. See the [API Overview](../greyscript/api-overview.md#aptclient).

## Getting the core libraries

New players usually use a hackshop repository to install `metaxploit.so` and `crypto.so` into `/lib`. See [Your First Hour](../getting-started/first-hour.md).
