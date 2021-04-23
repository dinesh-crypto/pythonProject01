import re
from numpy import random

import pymysql
db = pymysql.connect(host="localhost", user='root', password='', database='bank')


print("welcome to the YesBank!")

class user:
    def __init__(self, amount):
        self.amount = 0

    def userdetails(self):
        print("Name:", name)
        print("Age:", age)


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
    x = db.cursor()
    x.execute("use bank")
    try:
        x.execute("create table bankdetails(name varchar(30), age int, phoneno int, email varchar(20))")
    except Exception as e:
        print(e)

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phoneno = int(input("Enter your phone Number:"))
    email = input("Enter your mail id:")

    x.execute("INSERT INTO bankdetails(name, age, phoneno, email) VALUES (%s, %s, %s, %s)", (name, age, phoneno, email))

    db.commit()
    x.execute("select * from bankdetails")
    c = x.fetchall()
    print(c)
    db.close()
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