class demo:
    a = 50
    global b1

    def display(self):
        b1=10
        print(demo.a - b1)

x = demo()
x.display()
