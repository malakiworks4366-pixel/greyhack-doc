# Greybel JS

<span class="gh-badge">Development</span> <span class="gh-badge">CLI</span>

**Greybel JS** is a GreyScript toolkit written in TypeScript. It lets you develop GreyScript outside the game — bundling multiple files, minifying, running code in a local mock environment, and transferring finished code into the game.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>ayecue</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/ayecue/greybel-js">github.com/ayecue/greybel-js</a></td></tr>
<tr><td>Install</td><td><code>npm i -g greybel-js</code></td></tr>
<tr><td>License</td><td>MIT</td></tr>
</tbody></table>

## Why use it

- **Split big projects.** Bundle many `.src` files into one build, working around the in-game character limit.
- **Minify.** Shrink large projects (the project reports savings of up to ~40%).
- **Test locally.** Run scripts in a mock environment with a simulated computer, network, and file system — no game needed.
- **Push to the game.** With the message-hook plugin installed, transfer files straight into Grey Hack.

## Commands

### `build` — transpile & bundle

```bash
greybel build <filepath> [output]
```

| Flag | Meaning |
|---|---|
| `-u, --uglify` | Minify output |
| `-b, --beautify` | Pretty-print output |
| `-i, --installer` | Emit an installer that recreates files in-game (uses `import_code`) |
| `-ci, --create-ingame` | Transfer files directly into Grey Hack |
| `-ev, --env-files <file...>` | Load environment-variable files |
| `-en, --exclude-namespaces <ns...>` | Skip namespaces during optimisation |

### `execute` — run in a mock/in-game environment

```bash
greybel execute <scriptfile>
```

| Flag | Meaning |
|---|---|
| `-d, --debug` | Enable the debugger |
| `-p, --params <params...>` | Pass program arguments |
| `-s, --seed <seed>` | Seed mock entity generation |
| `-et, --env-type <mock\|in-game>` | Choose the environment |

### `repl` — interactive shell

```bash
greybel repl
```

### `ui` — browser UI

```bash
greybel ui
```

A web interface for minifying, executing, and sharing code.

### `import` — push files in-game

```bash
greybel import <targetpath>
```

Requires the message-hook plugin (see [Mods](mods.md)).

## Dependency management

Greybel extends vanilla imports (all compile back to standard GreyScript):

```greyscript
import { myNamespace } from "path/to/file"   // scoped import
#include "path/to/file"                        // inline paste
import_code("path/to/file")                    // keep separate in-game
```

## Syntax sugar

Block comments (`/* */`), trailing commas, shorthand operators (`+= -= *= /=`), bitwise operators (`<< >> | &`), and special expressions (`#filename`, `#line`, `#envar`, `#inject`). See [Imports & Libraries](../greyscript/imports.md).

## Environment variables

```bash
greybel build file.src --env-files env.conf
greybel execute file.src --env-vars TEST="hello world"
```

```greyscript
print(#envar MY_TEST_VAR)
```
