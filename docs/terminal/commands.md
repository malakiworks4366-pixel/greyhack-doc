# Command Reference

The built-in commands available in a standard Grey Hack terminal. Exact availability can vary with game version. Run `help` in-game for your current list.

## File system

| Command | Description |
|---|---|
| `ls [path]` | List files and folders. |
| `cd <path>` | Change the current directory. |
| `pwd` | Print the working directory. |
| `cat <file>` | Print a file's contents. |
| `mkdir <path>` | Create a folder. |
| `touch <file>` | Create an empty file. |
| `cp <src> <dst>` | Copy a file or folder. |
| `mv <src> <dst>` | Move or rename. |
| `rm <path>` | Delete a file or folder. |
| `chmod <perms> <file>` | Change permissions. |
| `clear` | Clear the screen. |

## Networking

| Command | Description |
|---|---|
| `ifconfig` | Show network interfaces, local/public IP, and gateway. |
| `nslookup <domain>` | Resolve a domain to an IP and vice versa. |
| `whois <ip>` | Show registration info for an address. |
| `ping <ip>` | Check whether a host responds. |
| `scp <src> <dst> <ip>` | Copy a file to or from a remote host. |
| `ssh <user@ip>` | Open an SSH session (if you have credentials). |
| `ftp <ip>` | Open an FTP session. |

## Wi-Fi

| Command | Description |
|---|---|
| `iwlist [iface]` | List nearby wireless networks (BSSID, ESSID, power). |
| `airmon <start\|stop> <iface>` | Toggle monitor mode. |
| `aireplay <bssid> <essid>` | Capture packets/ACKs from a network. |
| `aircrack <file.cap>` | Recover a password from a capture. |

See [Wi-Fi](../gameplay/wifi.md) for the full workflow.

## Users and processes

| Command | Description |
|---|---|
| `whoami` | Show the current user. |
| `sudo <command>` | Run a command as root (needs the password). |
| `passwd <user>` | Change a user's password. |
| `useradd` / `userdel` | Manage users. |
| `groupadd` / `groupdel` | Manage groups. |
| `ps` | List running processes. |
| `kill <pid>` | Terminate a process. |
| `reboot` | Reboot the machine. |

## Programs and building

| Command | Description |
|---|---|
| `build <src> <folder>` | Compile a `.src` file into a binary. |
| `./<binary>` | Run a compiled program. |
| `apt-get <...>` | Package manager — see [apt-get](apt.md). |

!!! note "Scripting replaces most commands"
    Nearly every command has a GreyScript equivalent (for example `get_shell.build`, `computer.File`, `get_router`). See the [API Overview](../greyscript/api-overview.md).
