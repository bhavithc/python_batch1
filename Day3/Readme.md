# Day3

### Print on console 
```python
print("Hello world")
```

### Satement
Programming instructions are called statements nothing else
```python
print("Hello world")
a = 10
b = 20
c = a + b # expression (a + b)
```

### Comments in python
#### Single line 
```python
# Single line comments 
a = 10 # 10 is assigned to a 

# Add two numbers 
# a: first number 
# b: second number 
def add(a, b):
    return a + b

# or 
""" This is multiline comments in 
program

Add two numbers 
a is first number
b is off number
return sum of a and b
"""
def sum(a, b):
    return a + b
```

### Variables 
- Must start with letter or underscore character
- Cannot start with number 
- No symbols are allowed apart from under score (A to Z) or (a to z) or (0 to 9) or (_)
- case sensitive (name and NAME and Name and namE all are different)
- Don't use keywords 
```python
import keyword
print(keyword.kwlist)
print("-" * 30)
print(keyword.softkwlist)
```
output:
```bash
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
------------------------------
['_', 'case', 'match', 'type']
```

#### Assign values to variable 
```python
a = 10
name = "Dilip"
```

#### Assign multiple values 
```python
a = b = c = 10 # a, b, c are points to integer object 10

a, b, c = 20 # a, b, c are points to interger object 20
``` 

### Useful functions 

*help*: provides a helpful message for python builtins

*type*: Returns the type of the object
```python
>>> a = 10
>>> type(a)
<class 'int'>
>>>
>>> b = 20.2
>>> type(b)
<class 'float'>
>>>
>>> c = True
>>> type(c)
<class 'bool'>
>>>
>>>
>>> d = "Hello"
>>> type(d)
<class 'str'>
```

*id:*
`id(obj)` -> Returns identity of the object
```python
>>> a = 10
>>> id(10)
4353192192
```

*dir*: Returns the names in current scope. In simple it prints supported functions and variable which we can use
```python
dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
```

```python
>>> a = 10
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
>>> type(a)
<class 'int'>
```

### Important notes
```python
a = 10
b = 10
```

- In the above code `a` is a variable of type integer, where in `a` points to an integer object (`int`) whose value is 10
- When `b = 10` that means `b` also now points to same integer object where `a` points to and whose value is `10`. 
*Summary:* Both `a` and `b` points to same integer object

### How to take input from the user 

use `input` function, that's it, and also you can assign to some variable

Example

```python
>>>
>>>
>>> name = input("what is your name? ")
what is your name? Bhavith
>>> age = input("What is your age? ")
What is your age? 29
>>>
>>> name
'Bhavith'
>>> age
'29'
>>>
```
Example2
```python
>>> # first way
>>> print("What is your name")
What is your name
>>> name = input()
Bhavith
>>> print("What is your age")
What is your age
>>> age = input()
29
>>> print(name, age)
Bhavith 29
>>>
>>> # second way
>>> name = input("What is your name?")
What is your name? Bhavith
>>> age = input("What is your age ")
What is your age 29
>>> print(name, age)
 Bhavith 29
>>>
```

> Note: if you want to convert what the user input's using `int()` is its number or `float()`
Example:
```python
>>> a = "120"
>>> type(a)
<class 'str'>
>>> b = int(a)
>>> type(b)
<class 'int'>
```

### How to print on console ? 

use `print` function/method 

Example:

```python
>>> # Print simply a string literal
>>> print("Hello world")
Hello world
>>>
>>> # Print multiple stuffs
>>> print ("Hi", "how", "are", "you", "?")
Hi how are you ?
>>>
>>> # print numbers
>>> print(10, 20, 12.34)
10 20 12.34
>>>
>>>
>>> # print variables
>>> a = 10
>>> print(a)
10
>>>
>>> # Mix variable and numbers
>>> a = 10
>>> print("a is ", a)
a is  10
>>>
>>>
>>> # format using string format
>>> name = "bhavith"
>>> age = 29
>>> print("My name is {} and age is {}".format(name, age))
My name is bhavith and age is 29
```

#### Postional print 
> Note: carefully look at the positions 
```python
>>> # using postional formatting
>>> print("My age is {1} and name is {0}".format(name, age))
My age is 29 and name is bhavith
```

### Multiline strings
```python
>>> print("""Hello guys, My name is Bhavith
...
... I am not 29 years old, actullay I am 35
... lol. This is how we can write the multi
... line string and also we can give spaces        like this    and it is still valid
... also I can give brace open (, close ). What ever I am writing here
...
...
... comes as it is. at the end close with three double quotes""")
Hello guys, My name is Bhavith

I am not 29 years old, actullay I am 35
lol. This is how we can write the multi
line string and also we can give spaces        like this    and it is still valid
also I can give brace open (, close ). What ever I am writing here


comes as it is. at the end close with three double quotes
```


## Assignments 
1. In the below program make user to enter the name in next line, instead of next to "What is your name?"
```python
name = input("What is your name?")
```

2. In the below program as soon as user type 9 it prints the message "what is your age" fix this program
```python
>>> age = input("what is your age\n")
what is your age
what is your age
what is your age
29
```

3. Ask for the user's name and print a personalised greeting.
4. Km to miles converter: read km, print miles (×0.621371)
5. Area and perimeter of a rectangle from user input.
6. Two numbers: print sum, difference, product, quotient. (Validate all the user inputs like work with zeros, and one's)
7. Tip calculator: bill + tip % → total to pay.

