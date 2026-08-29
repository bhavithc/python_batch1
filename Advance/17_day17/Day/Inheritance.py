class Parent:
    def __init__(self, name: str):
        print("Init of parent called")
        self._name = name

    def __del__(self):
        print("Del of parent called")

    def name(self):
        print(self._name)


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
        self._name = 10
        print("Init of child is called")

    def __del__(self):
        super().__del__()
        print("Del of child is called")

    def bar(self):
        print(self._name)


p = Child(name='Dilip')
p.bar()

del p