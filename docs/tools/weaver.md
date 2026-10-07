# Weaver

<span class="gh-badge">Utility</span> <span class="gh-badge">Rshell</span>

**Weaver** is a reverse-shell handler for Grey Hack. It helps manage `rshell` connections from a single interface and build reusable connection templates.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>Jcp22034</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/Jcp22034/Weaver">github.com/Jcp22034/Weaver</a></td></tr>
<tr><td>Status</td><td>Not actively developed; last tested on game 0.8.5108a (March 2024)</td></tr>
</tbody></table>

!!! info "What a reverse shell is in Grey Hack"
    The game models `rshell` (reverse shell) as a legitimate connection type on port **1222**: a target machine connects back to an `rshell` server you run, giving you a session. Weaver organises the server side and the templates that establish those connections.

## Features

- Build connection payloads from reusable templates.
- Manage reverse-shell process names on connected systems.
- Keep persistent `rshell` sessions.
- Extract account, credential, and network data from a session.
- Clean-up helpers for logs.

## Setup

1. Compile `Weaver.src`.
2. Ensure `metaxploit.so`, `crypto.so`, and `librshell.so` are in `/lib`.
3. Forward the `rshell` port on your router (default **1222**).

Templates use the `.wt` extension and live in `Weaver/Templates`, with the form:

```text
$.rshell_client("*IP*", *PORT*, "*PROCESS_NAME*")
```

See [Default Ports](../gameplay/ports.md) for the port table and [Libraries & Exploits](../gameplay/exploits.md) for the underlying API.
