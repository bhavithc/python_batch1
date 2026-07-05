
def sum_of_all_values(*values):
    print(type(values))
    sum = 0
    for value in values:
        sum = sum + int(value)

    return sum


sum_of_all_values(0, 1, 2, 3, 4)

# print(sum_of_all_values((0, 1, 2, 3)))

def my_print(*args):
    for arg in args:
        if isinstance(arg, int):
            print(arg, end=' ')
        elif isinstance(arg, float):
            print(arg, end=' ')
        elif isinstance(arg, str):
            print(arg, end=' ')
        elif isinstance(arg, list):
            print("\n")
            print("-------")
            for v in arg:
                print(v)
            print("-------")
        else:
            print("Unsupported")

my_print(10, 20, 30, ["hello", "world"])