# PEP8 standards 

## Create venv 
```bash 
python3 -m venv .venv
```
> Note: .venv can be any name ex: .dilip also 
> . (dot) says its a hidden directory 

## activate venv 
Windows
```bash
.\venv\Scripts\activate
```
Linux
```bash
source venv/Scripts/activate
```

## Install autopep8 
```bash
# Be inside venv and execute
pip install autopep8
```

**To format the source code**
```bash
autopep8 --in-place --aggressive --aggressive hello_world.py
```





| Type | Operators |
| -----| ----------|
| Artihmetic | +, -, *, /, %, //, **|
| Relational | <, >, <=, >=, ==, != |
| Logical | and, or, not |
| Bitwise | &, |, ^, ~, <<, >> |
| Assignment | =, +=, -=, *=, %= |
| Ternary | x if condition else y |
| Identitiy | is, is not | 

**if, elif, else**
```python
age = 20
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Falsy: False None 0 0.0 "" [] {} set()
if [0]: print("will run — list has one item")
```

**for** 
```python
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
for i in range(0,10,2): print(i)
    # 0 2 4 6 8
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

for name, age in zip(["Alice","Bob"],[30,25]):
    print(name, age)
```

**While, break, continue**
```python
count = 0
while count < 5:
    print(count); count += 1
for n in range(10):
    if n == 5: break # exit loop
if n % 2 == 0: continue # skip evens
    print(n) # 1 3
```


Hands-On Exercises
1. FizzBuzz: 1-100, multiples of 3→Fizz, 5→Buzz, 15→FizzBuzz.
2. Number guessing game: random 1-100, hot/cold hints.
3. Print all primes up to 100.
4. Reverse a number without string conversion.
5. Largest of three numbers without max().



Legacy 

```python
def greet():
    print("Hello")

def wrapper():
    print("Before")
    greet()
    print("After")

wrapper()
```

New 
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
```

with arg
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

```python
@my_decorator
def add(a, b):
    return a + b

print(add(10, 20))
```

Timing calculation
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Took {end - start:.3f} seconds")

        return result

    return wrapper

@timer
def slow_task():
    time.sleep(2)

slow_task()
```


### Variable Scopes in Python

Python follows the LEGB rule:

* L → Local
* E → Enclosing
* G → Global
* B → Built-in

example
```python
x = "global"

def outer():
    y = "enclosing"

    def inner():
        z = "local"
        print(x, y, z)

    inner()

outer()
```

Local Variable

Variables created inside a function are local by default.

```python
def func():
    x = 10
    print(x)

func()
```

try outside function
```python
print(x)
```

**The Problem: Modifying an Outer Variable**
```python
def outer():
    count = 0

    def inner():
        count += 1  # Error!

    inner()
```
> Note: it assumes count is a new local variable inside inner().

**Using nonlocal**
```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()

outer()
```
> Note: nonlocal count tells Python: “Don’t create a local variable. Use the count from the enclosing function.”

**Difference Between global and nonlocal**

**global**

Modifies a module-level variable.
```python
count = 0

def func():
    global count
    count += 1

func()
print(count)
```

**nonlocal**

Modifies a variable in the nearest enclosing function.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)

outer()
```

Practical Example: Counter
```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()

print(counter())
print(counter())
print(counter())
```

```bash
1
2
3
```

Here count survives between calls because the inner function forms a closure over the outer variable.

**Summary**

| Key word | Scope modified | 
|  - | - | 
| (none) | Local variable | 
| global | Module/global scope |
| nonlocal | Enclosing function scope |

