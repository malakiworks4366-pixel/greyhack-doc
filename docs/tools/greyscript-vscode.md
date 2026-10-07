# GreyScript (VS Code)

<span class="gh-badge">Development</span> <span class="gh-badge">VS Code</span>

A lightweight VS Code extension by **WyattSL** focused on syntax highlighting and small quality-of-life features for GreyScript. A simpler alternative to [Greybel VS](greybel-vs.md) if you only want highlighting.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>WyattSL</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/WyattSL/greyscript">github.com/WyattSL/greyscript</a></td></tr>
<tr><td>Install</td><td>VS Code Marketplace — search "Greyscript"</td></tr>
<tr><td>License</td><td>Apache-2.0</td></tr>
</tbody></table>

## Features

- **Syntax highlighting** for `.gs` and `.src` files (auto-activates).
- **Goto Error** command that maps Grey Hack's reported error line numbers to the real line in your source, working around the game's line-numbering quirks.
- **Minify** command for optimisation.
- **JSDoc support** recognising `@description`, `@param`, `@return`, `@author`, `@example`, `@deprecated`, and `@readonly`.

## Usage

Highlighting turns on automatically for supported files. To toggle it manually, press ++ctrl+k++ ++ctrl+m++ and pick "Greyscript". Open the command palette (++ctrl+shift+p++) and type `Greyscript:` to see its commands. Settings let you disable individual features.

!!! tip
    The same author maintains [greydocs](https://github.com/WyattSL/greydocs), an unofficial documentation site that includes the default [port table](../gameplay/ports.md) used here.
