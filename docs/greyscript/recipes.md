# Recipes

Short, reusable GreyScript snippets. Adapt paths and names to your game version.

## Print your own addresses

```greyscript
c = get_shell.host_computer
print("public: " + c.public_ip)
print("lan:    " + c.local_ip)
```

## Read a file safely

```greyscript
f = get_shell.host_computer.File("/etc/passwd")
if f == null then
  print("not found or no permission")
else
  print(f.get_content)
end if
```

## Loop over LAN devices

```greyscript
router = get_router("1.2.3.4")
if router != null then
  for ip in router.devices_lan_ip
    print(ip)
  end for
end if
```

## Simple argument parser

```greyscript
if params.len < 2 then exit("Usage: tool <ip> <port>")
ip = params[0]
port = params[1].to_int
print("target " + ip + ":" + port)
```

## A reusable menu

```greyscript
menu = function(title, options)
  print(title)
  for i in options.indexes
    print("[" + i + "] " + options[i])
  end for
  choice = user_input("> ").to_int
  if choice < 0 or choice >= options.len then return null
  return options[choice]
end function

pick = menu("Choose:", ["Scan", "Report", "Quit"])
print("you picked: " + pick)
```

## Format a table

```greyscript
rows = ["IP;PORT;SERVICE", "1.1.1.1;22;ssh", "1.1.1.1;80;http"]
print(format_columns(rows.join(char(10))))
```

!!! tip
    For the full list of functions and their exact signatures and return values, see the [API Overview](api-overview.md) and [documentation.greyscript.org](https://documentation.greyscript.org).
