def foo():
    x = 10
    print(f"FOO: add: {hex(id(x))}, value: {x}")

    def bar():
        nonlocal x
        x = 20
        print(f"BAR: add: {hex(id(x))}, value: {x}")

    bar()
    print(f"FOO: add: {hex(id(x))}, value: {x}")

foo()
