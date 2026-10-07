# Clojette

<span class="gh-badge">Language</span>

**Clojette** is a Clojure-like Lisp implemented in GreyScript / MiniScript. Its author built it in about four days as an alternative to plain GreyScript, independently of [Glosure](glosure.md).

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>lattiahirvio</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/lattiahirvio/Clojette">github.com/lattiahirvio/Clojette</a></td></tr>
</tbody></table>

## Features

- Runtime-expanded **macros** and **quasiquoting**
- **Splice unquoting** and **threading macros**
- **MiniScript interop**
- Keywords, `let` bindings, string literals
- An environment model based on *Structure and Interpretation of Computer Programs* (SICP)

## Usage

=== "Quick REPL"

    Copy `all.gs` into the game for a ready-to-use REPL.

=== "From source"

    Build the files in `/src/` with [Greybel](greybel-js.md) or compile manually. The standard library is recommended; the test suite is optional.

!!! note "Relation to Glosure"
    Clojette's author credits [Glosure](glosure.md) as the first Lisp implemented in GreyScript. The two are independent efforts to bring Lisp to Grey Hack.
