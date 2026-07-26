# Python Lists and Decorators - Practice Questions

## 1. Find the Second Largest Element (Without `sort()`)

### Question
Given a list of integers, find the second largest element.

### Input
```python
nums = [10, 5, 20, 8, 15]
```

### Output
```python
15
```

---

## 2. Remove Duplicates While Preserving Order

### Question
Remove duplicate elements from a list without changing the order of the first occurrence.

### Input
```python
nums = [1, 2, 3, 2, 4, 1, 5]
```

### Output
```python
[1, 2, 3, 4, 5]
```

---

## 3. Rotate a List by K Positions

### Question
Rotate the list to the right by `k` positions.

### Input
```python
nums = [1, 2, 3, 4, 5]
k = 2
```

### Output
```python
[4, 5, 1, 2, 3]
```

---

## 4. Find Common Elements in Two Lists

### Question
Find all common elements between two lists without using `set`.

### Input
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
```

### Output
```python
[4, 5]
```

---

## 5. Flatten a Nested List

### Question
Convert a nested list into a single flat list.

### Input
```python
data = [1, [2, 3], [4, [5, 6]], 7]
```

### Output
```python
[1, 2, 3, 4, 5, 6, 7]
```

---

## 6. Logger Decorator

### Question
Write a decorator that prints a message before and after a function executes.

### Input
```python
@logger
def greet():
    print("Hello")

greet()
```

### Output
```text
Starting greet
Hello
Finished greet
```

---

## 7. Execution Time Decorator

### Question
Write a decorator that measures the execution time of a function.

### Input
```python
@timer
def process():
    time.sleep(1)

process()
```

### Output
```text
process took 1.00 seconds
```

---

## 8. Function Call Counter Decorator

### Question
Write a decorator that counts how many times a function is called.

### Input
```python
@count_calls
def greet():
    print("Hello")

greet()
greet()
greet()
```

### Output
```text
Call #1
Hello
Call #2
Hello
Call #3
Hello
```

---

## 9. Repeat Decorator

### Question
Write a parameterized decorator `@repeat(n)` that executes a function `n` times.

### Input
```python
@repeat(3)
def hello():
    print("Hello")

hello()
```

### Output
```text
Hello
Hello
Hello
```

---

## 10. Cache Result Decorator

### Question
Write a decorator that caches function results and avoids recomputation for the same arguments.

### Input
```python
@cache_result
def square(n):
    print("Computing...")
    return n * n

print(square(5))
print(square(5))
```

### Output
```text
Computing...
25
25
```

### Note
`Computing...` should appear only once because the second call should return the cached result.