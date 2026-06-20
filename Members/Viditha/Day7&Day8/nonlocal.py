def foo():
    x = 10
    y=0
    print(f"FOO: add: {hex(id(x))}, value: {x}")
    print(f"FOO: add: {hex(id(y))}, value: {y}")

    def bar():
        nonlocal x
        x = 30
        print(f"BAR: add: {hex(id(x))}, value: {x}")

    def glass():
        y=90
        print(f"glass: add: {hex(id(y))}, value: {y}") 

    def table():
        nonlocal y
        y=60
        print(f"table: add: {hex(id(y))}, value: {y}")       

    bar()
    print(f"bar: add: {hex(id(x))}, value: {x}")

    table()
    print(f"table: add: {hex(id(y))}, value: {y}")
foo()