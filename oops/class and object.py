class dinesh:

    def demo(self):
        print(self)

    def addition(self, a):
        c = a
        print(c)

    def subtraction(self, a, b):
        self.d = a - b
        print(self.d)

    def di (self, a, b):
        self.x = a / b
        print(self.x)


a = dinesh()
salary = int(input("Enter your salary:"))
age = int(input("Enter your age:"))
if age == 10:
    a.subtraction(a=salary, b=age)
a.demo()
a.addition(a=20)
a.di(a=salary, b=age)


def add():
    print("Ram")
add()


def Ram():
    print("BIX")
Ram()
