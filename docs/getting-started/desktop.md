# The Desktop & Apps

Your in-game computer has a desktop with several programs. Names and layout can vary slightly between game versions.

| App | What it does |
|---|---|
| **Terminal** | The command line. Most of the game happens here. |
| **File Explorer** | A graphical file browser with permission and ownership views. |
| **CodeEditor** | The GreyScript editor. It saves `.src` files and compiles binaries, and has an *Importable* option for `import_code` targets. |
| **Browser** | Visits in-game websites: shops, banks, mail providers, and hackshops. |
| **Mail** | Your in-game email. Missions and contracts arrive here. |
| **Notepad** | A simple text editor. |
| **Map** | A visual map of the networks you have discovered. |
| **Settings** | Game and desktop preferences, such as wallpaper, sounds, and terminal colours. |

## File system layout

```text
/
├── bin/        # executables (ls, cd, ssh, …)
├── boot/       # kernel and system files
├── etc/        # configuration (passwd, apt sources, …)
├── home/       # user home directories
├── lib/        # shared libraries (*.so): metaxploit, crypto, net, …
├── root/       # root's home directory
├── sys/
├── usr/
└── var/        # logs (system.log)
```

!!! tip
    Many community tools expect `metaxploit.so` and `crypto.so` to be in `/lib`. They also often keep their files in a home or `/root` subfolder; 5hell, for example, uses `/root/rkit`.
