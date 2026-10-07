# Kore

<span class="gh-badge">Automation</span> <span class="gh-badge">Part of 5hell</span>

**Kore** is [5hell](5hell.md)'s setup and automation helper, named for the goddess of the underworld — fittingly, "your guide to 5hell." It automates the repetitive preparation steps so you can get to work quickly.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>Plu70</td></tr>
<tr><td>Ships with</td><td><a href="5hell.md">5hell</a> (<code>kore.5pk</code>)</td></tr>
<tr><td>License</td><td>MIT</td></tr>
</tbody></table>

## What it does

- **Builds the rkit folder.** `kore -r` creates `/root/rkit` and copies the files a toolkit needs there — `crypto.so`, `metaxploit.so`, and 5hell itself. If it can't find them, add them manually to `/lib` (libraries) and `/bin` (5hell).
- **Automatic secure-system setup.** Kore 3.0 can harden a system's configuration as part of its routine.
- **Guided workflow.** It walks you through the prompts needed to prepare a target or your own machine.

## Usage

Inside 5hell:

```text
|> kore -r      # set up the rkit folder (run this during first-time setup)
|> kore -h      # built-in help
```

Kore is normally the first thing you run after building 5hell. See the [5hell setup section](5hell.md#first-time-setup).
