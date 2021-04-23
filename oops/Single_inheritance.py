class dinesh:

    def demo(self):
        print(self)

    def addition(self, a):
        c = a
        print(c)

class B(dinesh):
    def subtraction(self, a, b):
        self.d = a - b
        print(self.d)

    def di (self, a, b):
        self.x = a / b
        print(self.x)

b=B()

salary = int(input("Enter your salary:"))
age = int(input("Enter your age:"))
if age == 10:
    b.subtraction(a=salary, b=age)
b.demo()
b.addition(a=20)
b.di(a=salary, b=age)

