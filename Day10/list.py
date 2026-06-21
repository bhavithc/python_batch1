fruits = ["apple", "orange", "banana", "grapes"]
print(hex(id(fruits)))

c = fruits
print(hex(id(c)))

# for fruit in fruits:
#     print(fruit)

fruits[0]= "pineapple"

print(fruits)

print(hex(id(fruits)))
print(hex(id(c)))


def update(local_fruits):
    local_fruits.append("lemon")


update(fruits)

print(fruits)


# a = 10
# b = 10

# b = 20

# print(hex(id(a)))
# print(hex(id(b)))
