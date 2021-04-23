from multipledispatch import dispatch

class demo:
    
    @dispatch(int,int)
    def mysum(a,b):
       print(a + b)

    @dispatch(int,int,int)
    def mysum(a,b,c):
       print(a * b * c)


o = demo()
o.mysum(4,5,2)
