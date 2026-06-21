"""
The single asterisk * packs any number of sequential positional arguments passed to the 
function into a single tuple
```python
def sum_numbers(*args):
    print(f"Data type: {type(args)}")  # Inside the function, 'args' is a tuple
    return sum(args)

# You can pass 2, 3, or any quantity of arguments
print(sum_numbers(10, 20))        # Output: 30
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15
```
"""

def sum_numbers(*args):
    print(f"Data type: {type(args)}")  # Inside the function, 'args' is a tuple

    sum = 0
    for i in args:
        sum = sum + i

    return sum

print(sum_numbers(1, 2, 3, 4))

