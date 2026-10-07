# Data Types

GreyScript has a small set of types. You can check a value's type with `typeof(x)`.

## Numbers

One numeric type covers integers and floats.

```greyscript
x = 42
y = 3.14
print(floor(y))      // 3
print(round(y, 1))   // 3.1
print(abs(-5))       // 5
print(rnd)           // random 0..1
```

Helpers include `ceil`, `sqrt`, `sign`, `str`, `val`, `to_int`, and the trig functions.

## Strings

```greyscript
s = "Grey Hack"
print(s.len)             // 9
print(s.upper)           // GREY HACK
print(s[0])              // G
print(s[1:4])            // rey
print(s.replace("Grey", "Great"))
print(s.split(" "))      // ["Grey", "Hack"]
print(s.indexOf("Hack")) // 5
```

Other useful methods: `lower`, `trim`, `to_int`, `code`, `values`, `remove`, `replace_regex`, `matches`.

## Lists

```greyscript
nums = [3, 1, 2]
nums.push(4)
nums.pop
nums.sort
print(nums.len)
print(nums.indexOf(2))
print(nums.join(", "))
total = nums.sum
```

Lists support slicing (`nums[1:3]`), `insert`, `remove`, `reverse`, `shuffle`, and `+` to concatenate.

## Maps

Maps are key/value structures, written with `{}`.

```greyscript
user = {"name": "Ada", "level": 7}
print(user.name)          // dot access
print(user["level"])      // bracket access
user.level = 8
print(user.hasIndex("name"))  // 1
print(user.indexes)           // keys
print(user.values)            // values
```

Maps are also how GreyScript does objects and classes — see [Functions & Objects](functions.md).

## Null

`null` is the absence of a value. Many API calls return `null` on failure, so test before using:

```greyscript
shell = get_shell
if shell == null then exit("no shell")
```

## Functions

Functions are values too and can be stored in variables and maps. See [Functions & Objects](functions.md).
