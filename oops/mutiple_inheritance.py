class A:
    a = 10
    b = 15
    def mt(self):
        print("Addition", A.a + A.b)

class B:

        print("Subtraction", A.a - A.b)

class C:

        print("Multiplication", A.a * A.b)

class D(A,B,C):

        print("Division", A.a // A.b)

a = D()
a.mt()