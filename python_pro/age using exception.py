a = int(input("enter the number"))

age = int(input("enter the number"))


def check():
    if (a % 2) == 0:
        print(a, "is even number")
    else:
        print(a, "odd number")


def age_check():
    try:

        if 18 < age < 40:
            print(age, "eligible to be ...")
        elif 45 < age < 70:
            print(age, "is eligible to")
        else:
            print(age, "not eligible")
    except Exception as m:
        print(m)
    else:
        print("")
    finally:
        pass

check()
age_check()
