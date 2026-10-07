# FAQ

## Is this the official documentation?

No. This is an unofficial, community-oriented site. The game is made by **Loading Home**. For the canonical GreyScript API, see [documentation.greyscript.org](https://documentation.greyscript.org).

## Where do I write GreyScript?

In-game with **CodeEditor**, or (recommended) in VS Code with [Greybel VS](../tools/greybel-vs.md) for autocomplete, debugging, and bundling. See [GreyScript](../greyscript/index.md).

## My script won't compile because it's too big. What do I do?

Grey Hack limits binary size. Split the project across files and use `import_code`, or let [Greybel](../tools/greybel-js.md) bundle and minify it for you. 5hell's `makfit` also shrinks binaries. See [Imports & Libraries](../greyscript/imports.md).

## Why do exploits stop working after an update?

Vulnerabilities are tied to **library versions**. When a library is patched to a newer version, old exploits for it no longer apply. Tools keep per-version exploit databases to cope. See [Libraries & Exploits](../gameplay/exploits.md).

## Which tool should I start with?

- Writing code: [Greybel VS](../tools/greybel-vs.md).
- A powerful all-in-one shell: [5hell](../tools/5hell.md).
- Just Wi-Fi: [Airlink](../tools/airlink.md).
- Browse everything in the [Player Tools directory](../tools/index.md).

## Are community tools safe?

Prefer tools whose source you can read, test them in single-player first, and keep backups. Native [mods](../tools/mods.md) patch the game client, so use trusted sources. See the warnings on those pages.

## A page here is out of date. Can I fix it?

Yes, please. See [Contributing](contributing.md).
