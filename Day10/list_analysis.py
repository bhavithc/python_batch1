fruits = ["apple", "banana", "grapes"]

print("fruits", hex(id(fruits)))

for fruit in fruits:
    print(" - ", fruit, " - ", hex(id(fruit)))


new_fruits = fruits.copy()
print("new_fruits", hex(id(new_fruits)))

for fruit in new_fruits:
    print(" - ", fruit, " - ", hex(id(fruit)))


# new_fruits.append("mango")
new_fruits[0] = "apples"
print("new_fruits", hex(id(new_fruits)))

for fruit in new_fruits:
    print(" - ", fruit, " - ", hex(id(fruit)))



fruits[1] = "orange"
print(fruits)
print(new_fruits)


for fruit in new_fruits:
    print(" - ", fruit, " - ", hex(id(fruit)))

