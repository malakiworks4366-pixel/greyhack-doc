# Securing Your Machine

In multiplayer, your computer is a target like any other. Hardening it is a core part of the game. This page is about **defence** — protecting what is yours.

## Checklist

- [ ] **Strong passwords.** Use long, non-dictionary passwords for every account. See [Passwords & Hashes](passwords.md).
- [ ] **Minimal services.** Every open port is an entry point. Only run services (SSH, FTP, HTTP) you actually need, and close the rest.
- [ ] **Patch your libraries.** Keep service libraries up to date so known vulnerabilities are fixed. Newer versions close holes that [exploits](exploits.md) rely on.
- [ ] **Tight firewall rules.** Configure your router's firewall to forward only the ports you intend to expose.
- [ ] **Correct permissions.** Lock down file and folder permissions with `chmod` so sensitive files aren't world-readable or writable.
- [ ] **Watch your logs.** Read `system.log` regularly to spot intrusions early. See [Logs](logs.md).
- [ ] **Back up.** Keep copies of important files somewhere a single compromise can't reach.

## Patching your own libraries

Newer game versions include a **Debug Library** (`metaLib.debug_tools`) that lets you scan your own libraries for weaknesses and apply patches:

```greyscript
metax = include_lib("/lib/metaxploit.so")
lib = metax.load("/lib/ssh.so")
dbg = lib.debug_tools
// inspect and patch vulnerable addresses
```

See the `metaLib` and `debugLibrary` entries in the [API Overview](../greyscript/api-overview.md).

## Hardening helpers in tools

Some community tools include defensive helpers. [5hell](../tools/5hell.md), for example, has a `lock` command for securing a system's permissions and a `bios` command for inspecting system objects. Use them on machines you own.
