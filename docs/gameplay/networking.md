# Networking Basics

## Public vs. LAN addresses

Every network has one **public IP**, which belongs to its router. Behind the router, devices have **LAN IPs** such as `192.168.x.x` or `10.x.x.x`.

- `get_shell.host_computer.public_ip` gives your public address.
- `get_shell.host_computer.local_ip` gives your LAN address.
- The script functions `is_lan_ip` and `is_valid_ip` help you validate addresses.

## Routers and switches

A **router** connects a LAN to the internet. In GreyScript, `get_router(ip)` returns a `router` object, which can list:

- `devices_lan_ip`: the devices behind it
- `used_ports`: ports forwarded through it
- `firewall_rules`: its firewall configuration
- `kernel_version`: the router's kernel library version

A **switch** (`get_switch(ip)`) groups devices inside a LAN. Some scanners, such as CerboScan, only see devices connected directly to a router.

## Port forwarding

Services on LAN machines are reachable from outside only if the router forwards a port to them. `router.ping_port(port)` and `port.get_lan_ip` tell you which LAN machine sits behind a forwarded port.

## Name resolution

- `nslookup` (command and function) resolves a domain to an IP.
- `whois` returns registration information for an address.

## Related tools

- CerboScan: LAN scanner
- 5hell: its `probe`, `lanpro`, `nsl`, `whois`, and `fwr` commands
