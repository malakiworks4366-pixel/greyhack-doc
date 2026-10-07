# Language Basics

## Variables and output

```greyscript
name = "Ada"
age = 36
print("Hello " + name + ", age " + age)
```

Variables need no declaration keyword. Assigning creates them.

## Comments

```greyscript
// single-line comment
```

[Greybel](../tools/greybel-js.md) also supports `/* block comments */`; they are removed when you build.

## Operators

| Kind | Operators |
|---|---|
| Arithmetic | `+ - * / % ^` |
| Comparison | `== != < > <= >=` |
| Logic | `and or not` |
| Membership | `isa`, `hasIndex` |

`true` and `false` are simply `1` and `0`.

## Conditionals

```greyscript
if age >= 18 then
  print("adult")
else if age >= 13 then
  print("teen")
else
  print("child")
end if

// single-line form
if age > 30 then print("over thirty")
```

## Loops

```greyscript
for i in range(1, 5)
  print(i)
end for

fruits = ["apple", "pear", "plum"]
for f in fruits
  print(f)
end for

n = 0
while n < 3
  n = n + 1
end while
```

`break` exits a loop, and `continue` skips to the next iteration.

## User input and parameters

```greyscript
answer = user_input("Your name: ")
secret = user_input("Password: ", true)   // second arg masks input

if params.len > 0 then print("First argument: " + params[0])
```

`params` is the list of command-line arguments passed to your program.

## Exiting

```greyscript
if params.len == 0 then exit("Usage: hello <name>")
```
