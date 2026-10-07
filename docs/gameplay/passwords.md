# Passwords & Hashes

Grey Hack models credentials the way a real Unix-like system does. Understanding the format is essential for scripting and for securing your own machine.

## Where credentials live

- User accounts are stored in `/etc/passwd`, one `user:hash` line per account.
- Service and account files (mail, bank) live in user home folders under a `Config` directory.

## Hashes and `decipher`

Stored passwords are not plain text; they are **hashes**. The `crypto.so` library exposes `decipher(user, hash)` which, given enough time, resolves a known hash back to its original text. Community tools wrap this with dictionaries and rainbow tables to make it practical.

```greyscript
crypto = include_lib("/lib/crypto.so")
result = crypto.decipher("root", theHash)
if result != null then print("recovered: " + result)
```

## Dictionaries and tables

Rather than brute-forcing every attempt live, players pre-generate **password tables** (mappings of text to hash). [5hell](../tools/5hell.md) includes several generators for this purpose: `pwgen` (a Markov generator), `cerebrum` (an onboard dictionary), `gopher` and `hashim` (hash resolvers that store results), and `jtr`.

## Changing passwords

With sufficient permissions, `computer.change_password(user, newPass)` and the `passwd` command update an account's credentials.

## Defending your own accounts

Choose long, non-dictionary passwords, and see [Securing Your Machine](security.md) for the full checklist.
