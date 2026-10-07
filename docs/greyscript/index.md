# GreyScript

**GreyScript** is Grey Hack's built-in programming language. It is a fork of [MiniScript](https://miniscript.org/), a small, readable scripting language, extended with game objects such as shells, computers, files, and networks.

| Page | Covers |
|---|---|
| [Language Basics](basics.md) | Variables, operators, control flow, comments |
| [Data Types](types.md) | Numbers, strings, lists, maps, null, functions |
| [Functions & Objects](functions.md) | Defining functions, maps as classes, `new`, `self`, `isa` |
| [Imports & Libraries](imports.md) | `import_code`, `include_lib`, and splitting projects |
| [Recipes](recipes.md) | Small, reusable snippets |

!!! tip "Write code outside the game"
    The in-game CodeEditor works, but most players write in VS Code with [Greybel VS](../tools/greybel-vs.md). It gives you autocomplete, error checking, a debugger, and bundling. The full API reference is at [documentation.greyscript.org](https://documentation.greyscript.org).

## Compiling

Save code as a `.src` file and compile it into a binary:

```text
build /home/me/hello.src /home/me/bin
```

From a script, use `get_shell.build(sourcePath, outputFolder)`. It returns an empty string on success, or an error message on failure.
