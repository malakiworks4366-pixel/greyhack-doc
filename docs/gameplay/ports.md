# Default Ports & Services

The common services and the ports they usually run on. The table is adapted from [WyattSL/greydocs](https://github.com/WyattSL/greydocs).

| Port | Service | Appears on | Installable by player |
|---:|---|---|:---:|
| 21 | FTP | Random | ✅ |
| 22 | SSH | Random | ✅ |
| 25 | SMTP | Email sites only | ❌ |
| 80 | HTTP | Random | ✅ |
| 141 | Bank (SQL) | Banks only | ❌ |
| 1222 | Rshell | Never (player-installed) | ✅ |
| 1542 | Repository | Hackshops | ✅ |
| 1883 | Smart appliance | Smart appliances | ❌ |
| 3306 | Criminals (SQL) | Police only | ❌ |
| 3307 | Students (SQL) | Schools only | ❌ |
| 3308 | Employees (SQL) | Random | ❌ |
| 5555 | ADB | — | ❌ |
| 6667 | Chat | Never (player-installed) | ✅ |
| 8080 | Router HTTP | All routers | ✅ |
| 37777 | CCTV | CCTV cameras | ❌ |

!!! info
    Every service is backed by a library (for example `ssh.so`, `ftp.so`, `http.so`) whose **version** decides which vulnerabilities it has. See [Libraries & Exploits](exploits.md).
