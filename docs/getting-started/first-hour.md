# Your First Hour

A checklist that gets a new player productive quickly.

## 1. Look around

- [ ] Open the **Terminal** and run `help` to list the built-in commands.
- [ ] Run `ls /`, `ls /bin`, and `ls /lib` to see the file system layout.
- [ ] Run `ifconfig` to see your local IP, public IP, and gateway.

## 2. Set up email and bank

Many missions and tools assume you have an in-game email account and a bank account. Use the **Mail** and **Browser** apps to register them.

## 3. Find a hackshop and get the core libraries

Much of the game's offensive scripting depends on two libraries:

| Library | Purpose |
|---|---|
| `metaxploit.so` | Analyse libraries for vulnerabilities and connect to remote services |
| `crypto.so` | Wi-Fi tools and password-hash deciphering |

You get them from in-game *hackshops*, which are servers that host an `apt-get` repository (see apt-get). Put them in `/lib`.

## 4. Get online

If you have no internet connection, see Wi-Fi.

## 5. Write your first script

Open **CodeEditor**, paste this, and save it as `/home/<you>/hello.src`:

```greyscript
print("Hello, Grey Hack!")
print("You are: " + active_user)
print("Your public IP: " + get_shell.host_computer.public_ip)
```

Compile it with `build hello.src /home/<you>` (or the editor's *Compile* button), then run `./hello`.

## 6. Level up your tooling

- Write code in VS Code with Greybel VS.
- Try a community shell such as 5hell.

## 7. Protect yourself

Before you go on the offensive in multiplayer, read Securing Your Machine.
