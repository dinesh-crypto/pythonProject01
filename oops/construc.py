class biggest:
    def __init__(self):
        self.a = int(input("Enter a number:"))
        self.b = int(input("Enter a number:"))

    def display(self):
        if self.a > self.b:
            print("a is the greatest number {}".format(self.a))
        else:
            print("b is the greatest number {}".format(self.b))

a = biggest()
a.display()
