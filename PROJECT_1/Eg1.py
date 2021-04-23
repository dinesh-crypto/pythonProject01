import re

from numpy import random

print("welcome to the YesBank!")

class user:
    def __init__(self, amount):
        self.amount = 0

    def userdetails(self):
        print("Name:", name)
        print("Age:", age)
        print("Phone Number:", phoneno)
        print("email:", email)

class bank(user):
    def __init__(self,amount):
        super().__init__(amount)
        self.a = self.amount

    def deposit(self):
        dep = int(input("Enter your deposit cash amount:"))
        self.a = self.a + dep
        print(self.a)
        print("deposited successfully")
        existinguser = int(input("3 Deposit: 4 withdrawl: 5 Check-Balance: 6 Exit:"))

        if existinguser == 3:
            x.deposit()

        if existinguser == 4:
            x.withdrawl()

        if existinguser == 5:
            x.checkbalance()

        if existinguser == 6:
            print("exit")

    def withdrawl(self):
        withdrl = int(input("Enter your withdrawl amount:"))
        if self.a >= withdrl:
            self.a = self.a - withdrl
            print(self.a)
        else:
            print("insufficient balance")
        print("withdrawl successfully")
        existinguser = int(input("3 Deposit: 4 withdrawl: 5 Check-Balance: 6 Exit:"))

        if existinguser == 3:
            x.deposit()

        if existinguser == 4:
            x.withdrawl()

        if existinguser == 5:
            x.checkbalance()

        if existinguser == 6:
            print("exit")

    def checkbalance(self):
        print("your balance is:", self.a)
        existinguser = int(input("3 Deposit: 4 withdrawl: 5 Check-Balance: 6 Exit:"))

        if existinguser == 3:
            x.deposit()

        if existinguser == 4:
            x.withdrawl()

        if existinguser == 5:
            x.checkbalance()

        if existinguser == 6:
            print("exit")



newuser = int(input("select 1 New Account or 2 Existing user"))

if newuser==1:
    print("please fill your details:")
    name = input("Enter your name:")
    if name<="a":
        x = re.search("^[A-Z]{1}[a-z]{20}$", name)
    else:
        print("invalid name please enter your First letter in uppercase")
    age = (input("Enter your age:"))
    phoneno = (input("Enter your phone no:"))
    if re.findall(r'[789]\d{9}$',phoneno):
        print(phoneno)
    else:
        print("Enter your 10 digit phone number")
    email = input("Enter your email-id:")
    print("your account number is-")
    print(random.randint(8, size=8))
    print("Your YES Bank account has been created successfully")

else:
    print("continue")

x = bank(0)

existinguser = int(input("3 Deposit: 4 withdrawl: 5 Check-Balance: 6 Exit:"))

if existinguser==3:
    x.deposit()

if existinguser==4:
    x.withdrawl()

if existinguser==5:
    x.checkbalance()

if existinguser==6:
    print("exit")
