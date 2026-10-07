# Glosure

<span class="gh-badge">Language</span>

**Glosure** is a LISP-like language for Grey Hack that executes arbitrary code at **runtime**, without recompiling. That makes it ideal for configuration and scripting inside tools like [5hell](5hell.md), where it powers the `macro` command.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>Maho_citrus</td></tr>
<tr><td>Known for</td><td>The first Lisp implemented in GreyScript; bundled with 5hell</td></tr>
</tbody></table>

## Why it matters

Normal GreyScript must be compiled into a binary before it runs. Glosure interprets its code live, so you can:

- Define macros that perform complex actions with a single command.
- Load custom scripts (for example via a `do.rc` file) without rebuilding your tools.
- Configure tools dynamically.

In 5hell, you load Glosure scripts through the `macro` command, and you can place them in your `do.rc` startup file. See the [5hell Command Reference](5hell-commands.md).

## Related projects

- **[Marinette](marinette.md)** — a shell configuration written entirely in Glosure.
- **[Riddle](https://github.com/shippingfandom/Riddle)** — a small programming language that transpiles to Glosure.
- **[Clojette](clojette.md)** — an independent Clojure-like Lisp for Grey Hack.
