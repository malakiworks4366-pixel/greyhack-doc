# Glossary

| Term | Meaning |
|---|---|
| **GreyScript** | Grey Hack's in-game scripting language, a fork of [MiniScript](https://miniscript.org/). |
| **MiniScript** | The small general-purpose language GreyScript is based on. |
| **`.src`** | A GreyScript source file. |
| **`.so`** | A compiled game **library** (shared object), e.g. `metaxploit.so`, `crypto.so`. |
| **metaxploit** | The core offensive library and its object; loads and analyses other libraries. |
| **metaLib** | A loaded library object you can scan for vulnerabilities. |
| **netSession** | A connection object to a remote service. |
| **Memory address** | A location in a library that may be vulnerable; exploited with a matching value. |
| **Shell** | A command session object on a computer. |
| **Rshell** | Reverse shell: a target connects back to a server you control (port 1222). |
| **Hackshop** | An in-game server hosting an `apt-get` repository of programs/libraries. |
| **BepInEx** | A Unity mod loader used for native Grey Hack [mods](../tools/mods.md). |
| **Message hook** | A plugin that lets external tools push files into the running game. |
| **Greybel** | ayecue's [CLI](../tools/greybel-js.md) and [VS Code](../tools/greybel-vs.md) toolkit for GreyScript. |
| **5hell** | Plu70's popular [shell/multitool](../tools/5hell.md). |
| **BUFFER** | 5hell's central object store, managed via `malp`. |
| **Glasspool** | 5hell's mechanism for running commands on a mirrored remote object. |
| **Glosure** | A [LISP-like runtime language](../tools/glosure.md) for Grey Hack. |
| **LAN IP** | A private address behind a router (e.g. `192.168.x.x`). |
| **Public IP** | A network's externally visible address (its router). |
| **Switch** | A device grouping machines inside a LAN. |
| **CTF** | Capture-the-flag; Grey Hack has related event objects (`ctfEvent`). |
