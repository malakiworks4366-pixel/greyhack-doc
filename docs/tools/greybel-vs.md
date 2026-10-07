# Greybel VS

<span class="gh-badge">Development</span> <span class="gh-badge">VS Code</span>

**Greybel VS** is the VS Code extension companion to [Greybel JS](greybel-js.md). It is the most full-featured way to write GreyScript, bringing autocomplete, diagnostics, an integrated interpreter, a debugger, and in-game building to the editor.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>ayecue</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/ayecue/greybel-vs">github.com/ayecue/greybel-vs</a></td></tr>
<tr><td>Install</td><td>VS Code Marketplace — search "Greybel"</td></tr>
<tr><td>License</td><td>MIT</td></tr>
</tbody></table>

## Features

- **Editing:** syntax highlighting for `.gs`, `.src`, and `.ms`; autocomplete; diagnostics; hover docs; formatter.
- **Build & deploy:** "Build file from context" transpiles and bundles; optional installer for projects over the character limit; "Auto create files in-game" via the message hook.
- **Run & debug:** integrated interpreter with mock and in-game environments, breakpoints, and a REPL.
- **Utilities:** a "Share" command (publishes to editor.greyscript.org), an in-editor API browser, snippets, output preview with TextMesh Pro rich-text rendering, and a colour picker for colour/mark tags.

## Command palette (Ctrl+Shift+P)

| Command | Action |
|---|---|
| `Greybel: Build file from context` | Transpile and bundle the current file |
| `Greybel: Run/Debug file from context` | Run or debug via the interpreter |
| `Greybel: Share` | Share code via editor.greyscript.org |
| `Greybel: API` | Open the GreyScript API browser |
| `Greybel: Snippets` | Insert a code snippet |
| `Greybel: Preview output` | Render TextMesh Pro tags |
| `Greybel: Import file into the game` | Upload a file directly |

## Settings

Grouped into general (toggles, file extensions, root file), create-in-game (enable, auto-compile, message-hook port), interpreter (default args, env vars, mock seed), transpiler (build type, formatting, optimisation, installer, watch mode), and type analyzer (dependency vs. workspace strategy, exclude globs).

## In-game integration (optional)

For in-game file creation and debugging, install **BepInEx** (5.x or 6.x) with the matching **GreyHackMessageHook** plugin. See [Mods](mods.md).

## Mock environment

The local environment simulates computers, networks, and a file system, with a hardcoded local machine (`root`/`test`) and pre-installed `crypto.so` and `metaxploit.so`, so you can test offensive scripts safely offline.
