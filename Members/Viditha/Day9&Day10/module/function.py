def add(a,b):
    return a+b

#print(dir(add))
def foo():
    print("inside foo")

def  add(a:int,b:int)-> int:
    return a+b
#print(add.__annotations__)
print(f"function name of function.py {add.__name__}") # add
" when excuting this function.py here _name_ will be main"
print(f"function.py  main consider this -{__name__}") # main

if __name__=="__main__":
    print("invoke directly")
    foo()
    print(f"this loop excutes only on Function.py run{__name__}")
else:
    print("invoke as module")    