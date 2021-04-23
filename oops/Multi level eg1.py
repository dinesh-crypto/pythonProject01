class A:
    a = 10
    b = 15
    def mt(self):
        print("Addition", A.a + A.b)

class B(A):

        print("Subtraction", A.a - A.b)

class C(B):

        print("Multiplication", A.a * A.b)

class D(C):

        print("Division", A.a // A.b)

a = D()
a.mt()



