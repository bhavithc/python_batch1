# Functions

```python
def add(a, b):
    return a + b
```

## Local 
Variables defined inside the current function
```python
x = 100

def foo():
    x = 10 # local variable 
    print(x)
foo()
```
> Note: Python finds x in the local scope, so it stops searching

## Enclosing
Variables in an outer function when functions are nested.
```python
def outer():
    x = 20 # Enclosing variable

    def inner():
        print(x) 
    
    inner()

outer()
```
> Note: Search order inside inner():
```
Local?      No
Enclosing?  Yes -> x = 20
If does not find in enclosing then it goes to global
```

## Global 
Variables defined outside all functions.
```python
x = 30

def foo():
    print(x)

foo()
```
> Note: Search order
```
Local?      No
Enclosing?  No
Global?     Yes -> x = 30
```

## Buil-in
Names provided by Python itself.

```python
print()
len()
sum()
min()
```
```python
my_list = [1, 2, 3]
print(len(my_list))
```

> Note: 
```
Local?      No
Enclosing?  No
Global?     No
Built-in?   Yes -> len()
```

# `local`, `global` and `nonlocal`

## local variable (No keyword)

A variable created inside a function belongs only to that function.

```python
x = 10

def func():
    x = 20   # Local variable
    print("Inside:", x)

func()
print("Outside:", x)
```
**Note:** The local x hides the global x.

## global variable `global`

Use the variable from the global scope, not create a new local one.

```python
x = 10
def func():
    global x # mark as global
    x = 20
func()
print(x)
```

## nonlocal variable `nonlocal`

- nonlocal is used with nested functions.
- Use the variable from the nearest enclosing function.

```python

def outer():
    x = 10
    def inner():
        nonlocal x # non local
        x = 20
    inner()
    print(x)
outer()
```

### Rule of thumb

| Keyword | Modifies Which Scope?| Used In | 
| - | - | - |
| (none) | Local scope | Any function |
| `global` | Global/module scope | Any function | 
| `nonlocal` | Nearest enclosing function scope | Nested functions only|

# Save function to variable 

- You can save the function as normal variable and can call it later
```python

```

# Day8 
