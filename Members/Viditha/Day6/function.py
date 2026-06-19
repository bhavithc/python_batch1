def add(a:int,b:int)-> int:
    print(type(a),type(b))
    return a+b

sum=int(add(10.5,20.5))
print(f"without type casting the individual variable{type(sum)}")

sum=add(int(10.5),int(20.5))
print(f"with type casting the individual variable{type(sum)}")

