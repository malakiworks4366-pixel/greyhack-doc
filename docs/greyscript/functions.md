# Functions & Objects

## Defining functions

```greyscript
greet = function(name, excited = false)
  msg = "Hello " + name
  if excited then msg = msg + "!"
  return msg
end function

print(greet("Ada"))
print(greet("Bob", true))
```

Parameters can have defaults. A function with no `return` yields `null`.

## Maps as objects

GreyScript has no `class` keyword. You build objects from maps, and `@` passes a function by reference instead of calling it.

```greyscript
Dog = {}
Dog.name = ""

Dog.bark = function()
  return self.name + " says woof"
end function

Dog.New = function(name)
  d = new Dog
  d.name = name
  return d
end function

rex = Dog.New("Rex")
print(rex.bark)   // Rex says woof
```

- `new Map` creates a copy that inherits from the original.
- Inside a method, `self` is the instance.
- `@name` references a function without invoking it, useful for callbacks and storing methods.

## Inheritance and type checks

```greyscript
Puppy = new Dog
Puppy.bark = function()
  return self.name + " says yip"
end function

spot = new Puppy
spot.name = "Spot"
print(spot.bark)        // Spot says yip
print(spot isa Dog)     // 1 — inherits from Dog
```

## Scope

Variables are local to the function unless they already exist in an outer scope. Use `globals` to reach the global scope and `locals` for the current one.
