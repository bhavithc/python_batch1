# 'append', 
# 'clear', 
# 'copy', 
# 'count', 
# 'extend', 
# 'index', 
# 'insert',
# 'pop', 
# 'remove', 
# 'reverse', 
# 'sort'

#           0.         1.     2          3
#          -4          -3      -2       -1
fruits = ["apple", "orange", "banana", "grapes"]


# append 
fruits.append("gauva")
print(fruits)

# fruits.clear()
# print(fruits)

new_fruits = fruits.copy()
print(new_fruits)


print(hex(id(fruits)))
print(hex(id(new_fruits)))

new_fruits[0] = "apples"

print(fruits)
print(new_fruits)

print(hex(id(fruits)))
print(hex(id(new_fruits)))


# print(fruits[0])
# print(fruits[-4])