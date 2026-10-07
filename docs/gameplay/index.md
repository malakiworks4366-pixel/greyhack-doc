# Gameplay

How Grey Hack's systems fit together. Each page explains a mechanic and links to the related API objects and community tools.

| Topic | You will learn |
|---|---|
| [Networking Basics](networking.md) | Public and LAN IPs, routers, switches, firewalls, port forwarding |
| [Default Ports & Services](ports.md) | Which services run on which ports |
| [Libraries & Exploits](exploits.md) | `metaxploit`, `metaLib`, memory addresses, and what an exploit can return |
| Wi-Fi | Getting online with `crypto.so` |
| Passwords & Hashes | `/etc/passwd`, hashes, and `decipher` |
| Logs & Covering Tracks | `system.log` and how traces work |
| Missions & Money | Contracts, banks, and the coin system |
| Securing Your Machine | Hardening your own system, especially in multiplayer |

## The typical loop

```mermaid
graph LR
  A[Find a target IP] --> B[Scan its ports and services]
  B --> C[Load the service's library]
  C --> D[Find vulnerabilities]
  D --> E[Get a shell, computer, or file object]
  E --> F[Complete the objective]
  F --> G[Clean up logs]
```

Community tools automate almost every step of this loop. See 5hell and the hacking utilities.
