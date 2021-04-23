class Add:
    def result(self):
        self.a = 30
        self.b = 40
        self.c = self.a + self.b
        print(self.c)

class Hello(Add):
    def __init__(self):
        super().result()

    def result(self):
        print("Hello world")

if __name__ == '__main__':
    x = Hello()
    x.result()