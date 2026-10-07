# 5hell Command Reference

Every command built into [5hell](5hell.md), grouped by purpose. Descriptions are taken from 5hell's own built-in `help` summary (5hell is MIT licensed, © Plu70).

!!! tip "In-game help"
    5hell has an extensive searchable help system. Type `help`, `help guide`, `help <topic>`, or `<command> -h` inside 5hell. Arcane's [Documentation Extractor](mods.md) can pull this help out for offline reading.


## Reconnaissance & networking

| Command | Description |
|---|---|
| `probe` | network probe. sumiltanious whois, fwr, lanpro, port info |
| `lanpro` | obtain a string of lan ips on a network |
| `nsl` | name server lookup. fetch ip for domain and vice versa |
| `whois` | return brief network info on a given ip or domain |
| `ping` | check to see if an ip responds. marginal actual use |
| `fwr` | obtain firewall rules from an ip |
| `sniff` | wait for ssh connections and print connection info |
| `smtp` | returns email info from an smtp server |
| `porter` | search a piped list of ips for a specific port |
| `ifconfig` | wireless and ethernet cli interface configuration |
| `iwlist` | view nearby wireless network essid, bssid, and pwr |
| `rnip` | produce a pipable string of random ips (for porter) |
| `ipfit` | create a string of random ip addresses for piping |
| `curl` | attempt to fetch website.html from piped object |
| `netdump` | dump net session data |
| `nt` | open a new terminal window |

## Exploitation

| Command | Description |
|---|---|
| `meta` | metalib and metaxploit management tool; essential |
| `db` | dbaser. the databaser tool. essential tool |
| `zap` | fire a single attack from a list of known exploits |
| `roil` | fire all known exploits at a linked metalib at once |
| `sphinx` | menu based hacking multi-tool |
| `linkdb` | load exploits from a database without linking a metalib |
| `liber` | obtain metalib version info for a file or folder |
| `dig` | dynamic infiltration gremlin. scriptable autohacker |
| `rshell` | place a reverse shell backdoor on a local machine |
| `rsi` | server to manage the above reverse shell backdoors |
| `infil` | upload rkit to a target and run 5hell |
| `fetch` | grab metaxploit object or log file from a shell |
| `zc` | zero chill. zero day assistant tool |

## Shells & sessions

| Command | Description |
|---|---|
| `ssh` | secure shell connection. supports brute force login |
| `psudo` | not-quite-sudo. get_shell and start_terminal tools |
| `glasspool` | glasspool mimic. shell/computer mirroring; essential |
| `shell` | print information about the active session |
| `whoami` | returns active user (or best guess in glasspool) |
| `prox` | tunnel through proxy nets to endpoint and start_terminal |
| `kraken` | batch rental proxy management. not meant for npc nets!! |
| `scrub` | shorcut to use kraken to clean all proxy system.logs |
| `target` | set target ip and port used by various commands |

## Password & hash tools

| Command | Description |
|---|---|
| `brutus` | brute force get_shell. escalation tool. req: cerebrum |
| `cerebrum` | magnum cerebrum. creates or imports onboard dictionary |
| `pwgen` | markov generator. writes password or hash:password files |
| `gopher` | hash cracker. supports strings and files. stores results |
| `hashim` | hash cracker daemon. stores results |
| `md5` | create or decipher a hash string without storing result |
| `jtr` | lightweight john the ripper random password generator |
| `dfit` | mothballed 'dictionary maker' tool |

## Files & editing

| Command | Description |
|---|---|
| `ls` | list files in a folder |
| `cat` | display text file contents. pipe to poke for concatenation |
| `cp` | copy file. respects glasspool |
| `mv` | move or overwrite a file or folder |
| `rm` | remove a file or folder |
| `mkdir` | make directory |
| `poke` | create/confirm a file. supports piping text into it |
| `tree` | recursive ls. adds hashes found to transmission buffer |
| `grep` | lightweight global regex printer. supports piped objects |
| `file` | cli file information tool. supports encrypt/decrypt |
| `felix` | file explorer |
| `scribus` | lightweight, MUD style, text editor tool |
| `append` | add text to the end of a file's contents or the clipboard |
| `diff` | compare two text files. useful for zero day puzzle |
| `chop` | a kinda weird way to slice/split text (wip) |
| `merge` | append the contents of file b to the bottom of file a |
| `sl` | symlink management tool |
| `flood` | spam a file x times |
| `make` | build a .src file |
| `makfit` | rebuild a .src until it's binary is under x bytes |
| `run` | launch an external binary. session is preserved |

## Memory, buffer & clipboards

| Command | Description |
|---|---|
| `malp` | memory alpha. object storage and management; essential |
| `buffer` | add anything to the buffer. supports all data types |
| `clipa` | alpha clipboard space. stores any data type |
| `clipb` | beta clipboard space. stores any data type |
| `clipc` | gamma clipboard space. stores any data type |
| `cob` | custom object tools. essential tool |
| `enum` | list enumeration and interation tool. built in 'do' |
| `purge` | session memory wipe tool. aka: the unbufferer |
| `memdump` | dump major memory objects to file |
| `string` | advanced string management tool |

## Permissions & users

| Command | Description |
|---|---|
| `usr` | add and remove users from a system |
| `grp` | view or change group params of users and files |
| `passwd` | change a user's password |
| `perms` | alter file permissions. includes a few presets |
| `lock` | secure a system's permissions. uses anti-brick technology |

## Logs & stealth

| Command | Description |
|---|---|
| `silentclean` | scrub log using mv. returns 1 on success |
| `rclean` | remote clean. copy-over a system.log on a piped object |
| `kore` | goddes of the dead, underworld, grain, and guide to 5hell |
| `cad` | cloak and dagger. produces a poisoned ps.src |
| `fakepass` | produces poisoned passwd.src |

## Data transfer

| Command | Description |
|---|---|
| `scpm` | scp menu. menu and cli upload/download management |
| `transmit` | send information to a hashim server via ssh |
| `tdump` | dump the transmission buffer (hashes) to file |

## Automation & scripting

| Command | Description |
|---|---|
| `do` | loop commands x times. supports strings and batch files |
| `enum` | list enumeration and interation tool. built in 'do' |
| `macro` | create macros to perform complex tasks with a single command |
| `glosure` | LISP like language for arbitrary runtime code execution |
| `if` | unintuitive but useful if statement processor |
| `cc` | carbon copy. invoke previous command from cli or menu |
| `pause` | pause script execution until a condition is met |
| `tws` | track while scanning. advanced BUFFEr querying |
| `dm` | daemon manager. manages daemons |
| `htop` | process monitor daemon |
| `ps` | list processes. highlights dsession, ps, 5hell |
| `kill` | terminate one or more processes by name or pid |

## Utility

| Command | Description |
|---|---|
| `echo` | returns it's input. useful for scripting |
| `calc` | calculator tools. includes padic representation tool |
| `time` | return up-time, game time, or game time and date |
| `bios` | display system information or manipulate system objects |
| `code` | multi-tool: ciphers, decompiler, char codes, function exec |
| `aptm` | open the apt-get menu. also has cli options |
| `mail` | herme5 mail system. supports login brute force |
| `herme5` | — |
| `games` | play blackjack, battleship, and Drug Wars |
| `credits` | gratitude |
| `contrib` | — |
| `help` | searchable help system for 5hell |
| `clear` | clear the screen |
| `cd` | change directory |
| `pwd` | print working directory |
| `cname` | returns the name of the active computer |
| `reboot` | reboot the machine |
| `quit` | exit |
| `outmon` | monitor a file for changes (mothballed) |

## Other

| Command | Description |
|---|---|
| `air` | open the air suite menu for wifi cracking |
| `osint` | open source intelligence. find an email |
| `pipe` | how piping works. piping itself is not a command |

!!! note
    This list reflects a recent 5hell release and may differ from your installed version. The authoritative reference is always 5hell's in-game `help`.
