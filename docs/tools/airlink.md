# Airlink

<span class="gh-badge">Utility</span> <span class="gh-badge">Wi-Fi</span>

**Airlink** is a polished, keyboard-driven terminal UI for Wi-Fi cracking in Grey Hack. It wraps the game's [Wi-Fi workflow](../gameplay/wifi.md) in a fast, mouse-free interface with a saved-key vault.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>VauL7Zer0</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/VauL7Zer0/airlink">github.com/VauL7Zer0/airlink</a></td></tr>
<tr><td>Built with</td><td><a href="greyscript-prime.md">GreyScript Prime</a></td></tr>
<tr><td>License</td><td>MIT</td></tr>
</tbody></table>

## Features

- **Zero typing.** Navigate entirely with arrow keys and function keys.
- **Key vault.** Store recovered network keys locally for reuse.
- **Auto Crack All.** Batch-process every visible network.
- **Blacklist.** Skip "burned" connections.
- **Telemetry.** Real-time signal info, WHOIS, and router details.
- **Themes.** Customisable, and sized to fit the default terminal window.

## Installation

Airlink expects a specific layout:

```text
/opt/airlink/
├── bin/airlink
├── etc/airlink.conf
└── lib/            # libAirlink.so, libGraphics.so, libHelp.so, libRam.so, libTheme.so, libUserInput.so

/home/<user>/Airlink/Theme/   # theme files
```

Build the library components and the `airlink` binary (the repository includes setup video tutorials), place them as above, then run `/opt/airlink/bin/airlink`.
