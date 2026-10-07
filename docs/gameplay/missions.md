# Missions & Money

## Where work comes from

Grey Hack gives you jobs in a few ways:

- **Mail missions.** Contracts arrive in your in-game **Mail** app. These range from simple file retrieval to more involved tasks.
- **Mission boards / agents.** In-game sites and NPCs offer contracts with payouts.
- **Multiplayer.** Other players may hire or trade with you.

## Banks and money

Money lives in in-game **bank accounts**, reachable through bank servers (SQL services on port 141). You register an account through the Browser, and your balance funds purchases from shops and hackshops.

## The coin / blockchain system

Grey Hack includes a crypto-currency system modelled on real blockchains, exposed through `blockchain.so`:

- `create_wallet` / `login_wallet` manage wallets.
- `coin_price`, `buy_coin`, `sell_coin` handle trading.
- Coins can be **mined** (`set_cycle_mining`, `amount_mined`, `get_reward`).
- Wallets have **subwallets** for organising funds.

See the `blockchain`, `wallet`, `coin`, and `subWallet` entries in the [API Overview](../greyscript/api-overview.md).

## Spending it

- **Shops** sell hardware and cosmetic items.
- **Hackshops** host `apt-get` repositories with programs and libraries — see [apt-get](../terminal/apt.md).
