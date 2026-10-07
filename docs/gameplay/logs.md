# Logs & Covering Tracks

Actions on a machine are recorded in its logs. In multiplayer especially, logs are how an administrator (or another player) notices an intrusion, so managing them is part of the game.

## The system log

Each machine keeps a `system.log` (under `/var`). It records logins, file changes, and similar events. Reading it is a legitimate part of defending a system: check your own `system.log` to see whether anyone has been poking at your machine.

## How traces work

When you connect through routers and proxies, each hop can record where the connection came from. Using intermediate machines (proxies) is the in-game way to make a connection harder to trace back.

## Cleaning up after yourself

The usual sequence after finishing on a target is:

1. Remove any files you created (tools, rootkits, temp files).
2. Replace or corrupt the relevant log so it no longer records your session.
3. Close your session.

Community tools automate this. In [5hell](../tools/5hell.md): `silentclean`/`sc` handles the local `system.log`, `rclean` handles a remote one, and `scrub` cleans proxy logs through `kraken`.

## Defensive angle

If you run services that other players can reach, read your logs regularly, keep backups of important files, and see [Securing Your Machine](security.md).
