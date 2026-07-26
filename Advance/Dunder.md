“Dunder” stands for Double UNDERscore.

They are special methods that Python automatically calls when certain operations happen.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Here `__init__` is Dunder method 

Common Dunder Methods 

| Method | Called when |
| - | - | 
| __init__ | Object creation |
| __str__ | print(obj) | 
| __repr__ | repr(obj) |
| __len__ | len(obj) | 
| __eq__ | == |
| __lt__ | < |
| __gt__ | > |
| __add__ | + |
| __getitem__ | obj[index] |
| __setitem__ | obj[index] = value |
| __iter__ | for x in obj |
| __next__ | Iterator next value | 
| __call__ | obj() |


Example 1: __str__
```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p)
```

Example 2: __len__
```python

class Playlist:
    def __init__(self):
        self.songs = ["A", "B", "C"]
    def __len__(self):
        return len(self.songs)
p = Playlist()
print(len(p))

```

Example 3: __eq__
```python
class Employee:

    def __init__(self, id):
        self.id = id
    def __eq__(self, other):
        return self.id == other.id

a = Employee(10)
b = Employee(10)
print(a == b)
```

Example 4: __add__

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

m1 = Money(100)
m2 = Money(50)

print((m1 + m2).amount)
```

Example 5: __call__
```python
class Multiplier:

    def __call__(self, x):
        return x * 2

m = Multiplier()

print(m(5))
```

# Dataclasses

Before Python 3.7, you often wrote a lot of repetitive code:
```python
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Imagine a class with 10 fields.

You would also want:
* constructor
* equality
* string representation
* ordering

Writing these repeatedly becomes tedious.

Python introduced dataclasses.

## Basic Dataclass

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int

e = Employee("John", 30)

print(e)
```

Output:
```bash
Employee(name='John', age=30)
```

Notice there is no __init__, Python generated it automatically.


**What Dataclass Automatically Generates?**

For 
```python
@dataclass

class Employee:
    name: str
    age: int
```

Python automatically creates:
```python
__init__()
__repr__()
__eq__()
```
without you writing them.

### Equality
```python
e1 = Employee("John", 30)
e2 = Employee("John", 30)
print(e1 == e2)
```
Output
```
True
```
Without @dataclass, these would not compare equal unless you implemented __eq__.

### String Representation

```python
print(Employee("Alice", 25))
```
Output
```bash
Employee(name='Alice', age=25)
```
No need for __str__ or __repr__.

### Mutable Default Values

Avoid this 
```python
@dataclass
class Student:
    marks: list = []      # Wrong
```
All instances would share the same list.

Correct approach:
```python
from dataclasses import dataclass, field

@dataclass
class Student:
    marks: list = field(default_factory=list)
```
Each instance gets its own list.

### Frozen Dataclass (Immutable)
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
p = Point(1, 2)

p.x = 10
```
Output
```bash
FrozenInstanceError
```

### Ordered Dataclass

```python
from dataclasses import dataclass
@dataclass(order=True)
class Employee:
    salary: int
    name: str

e1 = Employee(50000, "Alice")
e2 = Employee(60000, "Bob")
print(e1 < e2)
```

Output:
```bash
True
```

Note: Comparison methods like __lt__, __le__, __gt__, and __ge__ are generated automatically.

### __post_init__
Sometimes you need extra initialization after the generated __init__ runs.
```python
from dataclasses import dataclass

@dataclass

class Rectangle:
    width: int
    height: int
    area: int = 0

    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(10, 20)
print(r.area)
```
Output:
```bash
200
```

# Dunder Methods vs Dataclasses
| Dunder Methods | Dataclass|
| - | - | 
| Special methods called by Python automatically | Decorator that generates common dunder methods |
| You implement behavior manually | Python generates common behavior for you | 
| Used to customize operators, printing, iteration, indexing, etc. | Used to reduce boilerplate for classes that mainly store data| 
| Examples: __add__, __iter__, __call__, __getitem__ | Automatically creates __init__, __repr__, __eq__, and optionally ordering| 

### When to Use Which?

- Use dunder methods when you want custom behavior, such as making objects printable, iterable, comparable, callable, or usable with operators.
- Use @dataclass when your class is primarily a container for data and you want Python to generate common methods automatically.

### Difference between __str__ and __repr__

* __str__ → Human-readable representation (for end users)
* __repr__ → Developer/debug representation (for programmers)

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns ${self.salary}"

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

e = Employee("Alice", 50000)
```
