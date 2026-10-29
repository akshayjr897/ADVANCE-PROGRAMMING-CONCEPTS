class Calculator:
    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = Calculator()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)