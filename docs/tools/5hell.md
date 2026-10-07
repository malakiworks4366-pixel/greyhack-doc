# 5hell

<span class="gh-badge">Shell</span> <span class="gh-badge">Framework</span>

**5hell** (pronounced "shell") is the best-known player-made tool for Grey Hack: a shell emulator and all-in-one multitool with well over a hundred commands. It bundles reconnaissance, exploitation, password tooling, file management, automation, and stealth into a single scriptable environment.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>Plu70 (jhook777)</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/jhook777/5hell-for-Grey-Hack-the-Game">github.com/jhook777/5hell-for-Grey-Hack-the-Game</a></td></tr>
<tr><td>Discord</td><td><a href="https://discord.gg/AFqsGaCDfS">discord.gg/AFqsGaCDfS</a></td></tr>
<tr><td>License</td><td>MIT</td></tr>
<tr><td>Full command list</td><td><a href="5hell-commands.md">5hell Command Reference</a></td></tr>
</tbody></table>

## What it is

5hell is written in GreyScript and built from several source packages inside the game. Once compiled, you run it like any binary and get a custom prompt (`|>`) with its own command language. It is designed around a few powerful concepts rather than a pile of unrelated scripts.

## Core concepts

### The BUFFER and `malp`

The **BUFFER** is 5hell's central object store. Exploit results, shells, files, and any other objects land here, and you manage them through the `malp` (Memory Alpha) menu. The docs call it "the backbone of 5hell."

### Pipes

Commands chain with `|` (pipe) and `||` (chain without piping), passing one command's output into the next — "if malp is the backbone of 5hell, pipes are the circulatory system." Example:

```text
|> ifconfig -p | probe
```

### Glasspool

**Glasspool** mirrors a remote shell or computer object so your commands execute on the *target* instead of locally, without opening a terminal there. When active, the prompt turns blue.

### Easy Clip & the custom object

Short references like `@a`, `@b`, `@c` (clipboards), `@tbuf` (transmission buffer), and `@home` (home server) let you reference stored values inside commands. A shared *custom object* carries data between nested shell launches.

### Automation: `do` and `dig`

`do` runs batches of commands — a number of iterations, an inline block, or a script file — so almost everything can be automated. `dig` ("dynamic infiltration gremlin") is a scriptable auto-hacker that scans, exploits, and deploys. Together they can automate nearly the entire workflow.

### Prompts

| Prompt | Meaning |
|---|---|
| `|>` | Standard command line |
| <span style="color:#5bc0ff">`|>`</span> | Glasspool active (commands run on the target) |
| `:>` | Expecting a string input |
| `||:` | Single-keypress menu selection |

## Building 5hell

5hell is compiled from several `.5pk` packages in a specific order. You can do it by hand in the in-game CodeEditor, or in one click with [Greybel VS](greybel-vs.md).

!!! example "Manual build order"
    As root (`sudo -s`), create `/root/src`, then in **CodeEditor** (with *Importable* ticked) build each package into `/root/src`:

    1. `contrib.5pk`
    2. `net.5pk`
    3. `kore.5pk`
    4. `dtools.5pk`
    5. `5phinx.5pk`
    6. `help.5pk`
    7. `5hell.5pk`

    Finally build `5hell.src` into a binary **without** the *Importable* flag (e.g. to `/5hell`). Set your `access_codes` passwords in `5hell.src`, or delete that section for passwordless use.

After building, use the optional `makfit <path> 120000` to shrink the binary under a target size.

## First-time setup

```text
|> kore -r          # build the rkit folder; copies crypto.so, metaxploit.so, 5hell
|> pwgen | pwgen hash   # optionally generate password/hash tables
```

See [Kore](kore.md) for the setup helper, and the [5hell Command Reference](5hell-commands.md) for every command.

## A first target (quick version)

```text
|> probe 1.2.3.4     # whois + portscan, sets the 5phinx target
|> sphinx            # open the 5phinx pentest menu and work the target
```

Then manage results from the BUFFER via `malp`. The in-game `help guide` walks through the full flow.

## Included sub-tools

5hell ships with or integrates several other community projects: **[Kore](kore.md)** (setup/automation), **5phinx** (a menu-driven pentest tool), **[Glosure](glosure.md)** by Maho_citrus (runtime scripting via the `macro` command), and **[Marinette](marinette.md)** by Hecate (Glosure configuration).
