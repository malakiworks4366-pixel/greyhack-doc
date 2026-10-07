#!/usr/bin/env python3
import json, os, sys

META = sys.argv[1]  # path to greyscript-meta/src
SIG = os.path.join(META, "signatures")
DESC = os.path.join(META, "descriptions", "en")

TYPES = [
    ("general", "Global functions", "Functions available anywhere: shells, networking, I/O, math, strings, time."),
    ("shell", "shell", "A command session. Build binaries, launch programs, scp, connect to services."),
    ("computer", "computer", "A machine: files, users, groups, processes, network cards, Wi-Fi."),
    ("file", "file", "Files and folders: content, permissions, ownership, copy/move/delete."),
    ("metaxploit", "metaxploit", "The metaxploit.so toolkit: load libraries, open net sessions, scan memory."),
    ("metaLib", "metaLib", "A loaded library you can analyse for vulnerabilities.", "meta-lib"),
    ("netSession", "netSession", "A connection to a remote service.", "net-session"),
    ("crypto", "crypto", "The crypto.so toolkit: Wi-Fi tools and hash deciphering."),
    ("router", "router", "A router: LAN devices, forwarded ports, firewall rules."),
    ("port", "port", "A network port on a host."),
    ("file_ftp", "ftpShell", "An FTP session.", "ftp-shell"),
    ("string", "string", "String methods."),
    ("list", "list", "List methods."),
    ("map", "map", "Map methods."),
    ("number", "number", "Number helpers."),
    ("blockchain", "blockchain", "The blockchain.so toolkit for coins and wallets."),
    ("wallet", "wallet", "A crypto wallet."),
    ("aptClient", "aptClient", "The apt-get client object.", "apt-client"),
    ("ctfEvent", "ctfEvent", "CTF event helpers.", "ctf-event"),
    ("metaMail", "metaMail", "The in-game mail client.", "meta-mail"),
]

def load(name):
    stem = name
    return json.load(open(os.path.join(SIG, stem + ".json")))

def load_desc(stem):
    p = os.path.join(DESC, stem + ".json")
    return json.load(open(p)) if os.path.exists(p) else {}


def tstr(t):
    if isinstance(t, dict):
        base = t.get("type", "any")
        vt = t.get("valueType"); kt = t.get("keyType")
        if base == "map" and kt and vt: return "map<%s,%s>" % (tstr(kt), tstr(vt))
        if vt: return "%s<%s>" % (base, tstr(vt))
        return base
    return str(t)

def sig_str(name, d):
    args = d.get("arguments", [])
    parts = []
    for a in args:
        label = a["label"]
        t = a.get("type", "any")
        t = "|".join(tstr(x) for x in t) if isinstance(t, list) else tstr(t)
        if "default" in a:
            label = label + "?"
        parts.append(label + ": " + str(t))
    rets = d.get("returns", [])
    if isinstance(rets, list): rets = ", ".join(tstr(x) for x in rets)
    else: rets = tstr(rets)
    s = name + "(" + ", ".join(parts) + ")"
    if rets: s += " -> " + rets
    return s

out = []
out.append("# API Overview\n")
out.append("""A browsable summary of the GreyScript API, generated from [ayecue/greyscript-meta](https://github.com/ayecue/greyscript-meta) (MIT licensed). It lists each type and its members with signatures and a one-line description.

!!! info "Canonical reference"
    For full descriptions, examples, and the newest additions, use the official searchable docs at [documentation.greyscript.org](https://documentation.greyscript.org). This page is a convenient offline-style summary, not a replacement.

**Signature key:** `name(arg: type, optional?: type) -> returnType`. A `?` marks an optional argument.
""")

for entry in TYPES:
    key, title = entry[0], entry[1]
    blurb = entry[2]
    stem = entry[3] if len(entry) > 3 else key
    try:
        sig = load(stem)
    except FileNotFoundError:
        continue
    desc = load_desc(stem)
    out.append("\n## " + title + "\n")
    out.append(blurb + "\n")
    meta = desc.get("$meta", {})
    defs = sig.get("definitions", {})
    rows = []
    for mname, mdef in sorted(defs.items()):
        if mdef.get("type") != "function":
            continue
        s = sig_str(mname, mdef)
        d = desc.get(mname, {})
        dtext = d.get("description", "") if isinstance(d, dict) else ""
        # strip markdown links and html, collapse
        import re
        dtext = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", dtext)
        dtext = re.sub(r"`([^`]*)`", r"\1", dtext)
        dtext = re.sub(r"<[^>]+>", "", dtext)
        dtext = dtext.replace("\n", " ").strip()
        # first sentence
        if ". " in dtext:
            dtext = dtext.split(". ")[0] + "."
        dtext = dtext.replace("|", "\\|")
        rows.append((s, dtext[:180]))
    if not rows:
        continue
    out.append("| Signature | Description |")
    out.append("|---|---|")
    for s, d in rows:
        out.append("| `" + s + "` | " + d + " |")
    out.append("")

open("docs/greyscript/api-overview.md", "w").write("\n".join(out))
print("wrote api-overview.md", len("\n".join(out)), "bytes")
