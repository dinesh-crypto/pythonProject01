class Error(Exception):
 pass
class Toosmall(Error):
 pass
class Toolarge(Error):
 pass
number=10

while True:
    try:
        num=int(input("guess a number"))
        if num > number:
          raise Toolarge
        elif num < number:
            raise Toosmall
        break
    except Toolarge:
        print("This value is too large,try again")
        print()
    except Toosmall:
        print("This value is too small,try again")
        print()
print("you guessed correctly")


