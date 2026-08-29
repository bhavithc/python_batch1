from ravi import calc

def add(a, b):
    print("[DILIP] add is called")
    return calc.add(a, b)

def sub(a, b):
    print("[DILIP] sub is called")
    return a - b

class Mul:
    def __init__(self):
        print("Instance created ")