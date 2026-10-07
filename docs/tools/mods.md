# Message Hook & BepInEx Mods

<span class="gh-badge">Development</span> <span class="gh-badge">Native mod</span>

Some tools extend the Grey Hack **client itself** (not just scripts inside the game) using **BepInEx**, a popular Unity mod loader. The most important for developers is the **message hook**.

!!! warning "Use at your own risk"
    Native mods patch the game client. Use trusted sources, keep backups, and be aware that mods can break after game updates. They are generally for single-player / development use.

## GreyHackMessageHook

A BepInEx plugin that opens a local channel so external tools can push files into the running game. It is what powers [Greybel VS](greybel-vs.md)'s "create files in-game" and [Greybel JS](greybel-js.md)'s `import` command.

- Install **BepInEx** (5.x or 6.x) into your Grey Hack folder.
- Add the **GreyHackMessageHook** plugin.
- Point your tool at the configured port.

## Arc8ne's mods and libraries

[Arc8ne](https://github.com/Arc8ne) maintains several BepInEx projects:

| Project | Purpose |
|---|---|
| [GHPluginCoreLib](https://github.com/Arc8ne/GHPluginCoreLib) | A core library to help write Grey Hack BepInEx plugins |
| [Bank-Transfer-Utility-Program-Mod](https://github.com/Arc8ne/Bank-Transfer-Utility-Program-Mod) | Adds an in-game bank-transfer utility |
| [GH-Boot-Sequence-Animation-Skipper](https://github.com/Arc8ne/GH-Boot-Sequence-Animation-Skipper) | Skips the boot animation |
| [5hell-Documentation-Extractor](https://github.com/Arc8ne/5hell-Documentation-Extractor) | Extracts [5hell](5hell.md)'s built-in docs for offline reading |

## Terminal UI mod

[Greybel JS](greybel-js.md) also ships a "GreyHack Terminal UI" mod that extends GreyScript so scripts can draw custom GUI programs.
