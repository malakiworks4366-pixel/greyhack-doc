# Imports & Libraries

Grey Hack binaries have a size limit, so large projects are split into files. There are two separate ideas: **game libraries** and **code imports**.

## Game libraries: `include_lib`

`include_lib` loads a compiled `.so` game library and returns its object.

```greyscript
metax = include_lib("/lib/metaxploit.so")
if metax == null then exit("metaxploit.so not found")
```

Common libraries: `metaxploit.so`, `crypto.so`, `net.so`. See [Libraries & Exploits](../gameplay/exploits.md).

## Code imports: `import_code`

`import_code` pulls another source file into your program at build time. In vanilla GreyScript it looks like:

```greyscript
import_code("/home/me/lib/utils.src")
```

All `import_code` lines must be in the entry file. The imported files are compiled alongside it.

## Greybel's extended imports

[Greybel](../tools/greybel-js.md) adds friendlier dependency management that compiles down to vanilla GreyScript:

```greyscript
// pull exported members into a namespace, no global pollution
import { helper } from "lib/utils"

// paste the file's contents inline
#include "lib/constants"

// keep files separate in-game to dodge the character limit
import_code("lib/utils")
```

Greybel resolves relative paths, detects cyclic dependencies, and can generate an *installer* that recreates all files in-game.

## Project layout

A typical Greybel project:

```text
my-tool/
├── main.src          # entry point with imports
├── lib/
│   ├── utils.src
│   └── ui.src
└── env.conf          # optional environment variables
```

Build it with `greybel build main.src out/`. See [Greybel JS](../tools/greybel-js.md).
