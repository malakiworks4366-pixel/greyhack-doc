# Wi-Fi

When you start without a wired connection, you need to join a Wi-Fi network. The in-game workflow uses `crypto.so` and its matching terminal commands.

## Workflow

1. **List networks.** Run `iwlist <interface>` (usually `wlan0`) to list nearby networks with their BSSID, signal strength (PWR), and ESSID.
2. **Enable monitor mode.** Run `airmon start wlan0`.
3. **Capture packets.** Run `aireplay <bssid> <essid>` and let it collect enough ACKs. Stronger signals need fewer.
4. **Recover the key.** Run `aircrack file.cap` on the capture.
5. **Connect.** Use the network menu, or `computer.connect_wifi` in a script.

The same steps exist as `crypto` methods in GreyScript: `airmon`, `aireplay`, and `aircrack`. You can also use `computer.wifi_networks` and `computer.connect_wifi`.

## Related tools

- [Airlink](../tools/airlink.md): a full terminal UI with a key vault and "Auto Crack All"
- [5hell](../tools/5hell.md): its `air` and `iwlist` commands
