# 'count', 
# 'extend', 
# 'index', 
# 'insert',
# 'pop', 
# 'remove', 
# 'reverse', 
# 'sort'


# fruits = [ "orange", "banana", "grapes", "apple"]

# print(fruits.count("orange"))


# for s in "apple":
#     print(s)


# new_items = ["mango"]

# for item in new_items:
#     fruits.append(item)

# print(hex(id(fruits)))

# fruits.extend(["mango", "kiwi"])

# print(hex(id(fruits)))
# print(fruits)

# print(fruits.index("apple"))

# print(fruits)
# fruits.insert(-500, "kiwi")
# fruits.insert(-45, "dragon")
# fruits.insert(45, "dragon")
# print(fruits)


fruits = [ "orange", "banana", "grapes", "apple"]

# print(fruits)

# fruits.reverse()
fruits.sort()

# print(hex(id(fruits[0]))) # 0x01
# fruit = fruits.pop(0)     # 0x01
# print(hex(id(fruit)))     # 0x01

# fruits.remove("orange")
# print(fruits)

# def foo():
#     print("inside foo")
#     return 10

# def bar():
#     print("inside bar")

# mixed_list = ["apple", "ball", "cat", 1, 2, 3, [1, 2, 3], foo(), bar]

# for l in mixed_list:
#     if isinstance(l, int):
#         print("it is an integer")
#     elif isinstance(l, str):
#         print("it is string")
#     elif callable(l):
#         l()
#     elif isinstance(l, list):
#         print("it is a list")

#     print(l)

numbers = []

for i in range(0, 10):
    numbers.append(i)

print(numbers)

# even_list = []
# odd_list = []

# for number in numbers:
#     if number % 2 == 0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)

# print(even_list)
# print(odd_list)
    

# List comphrenstion
# new_numbers = [i for i in numbers]
# print(new_numbers)

c = 11
is_even_or_odd = ['even' if c % 2 == 0 else 'odd']
print(is_even_or_odd)


# even_list = []

# for number in numbers:
#     if number % 2 == 0:
#         even_list.append(number)


even_list = [number for number in numbers if number % 2 == 0]

print(even_list)