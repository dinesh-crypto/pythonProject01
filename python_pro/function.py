# in build
num1 = 10
num2 = 20


def sum(x, y):
    sum = x + y
    return sum


print("The sum is", sum(num1, num2))


# add
def sum(a, b):
    total = a + b
    return total


x = 10
y = 20
print("The sum of", x, "and", y, "is:", sum(x, y))


# user defined
def add(x, y):
    print("ADD of ", x, " and ", y, " is ", (x + y))


add(3, 4)

# sum
g = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def mysum(g):
    sum = 0
    for i in g:
        sum += i
    return sum


print(" the sum is ", mysum(g))
# dict
