import re
n = ['avi', ]
p = ['123', ]


class login():
    def newuser(self):
        print("create your new account")
        name = input('Enter a username:')

        password = input('Enter a password:')
        if name in n:
            print('Already existed')
        else:
            n.append(name)
            p.append(password)
            print("Created successfully")
            print(n)
            print(p)

            a = dict(zip(n, p))
            print("Login your account")
            name = input('Enter your username:')
            password = input('Enter your password:')
            if name in a.keys() and password in a.values():
                print("Login Successfully")



    def existinguser(self):
        a = dict(zip(n, p))
        print("Please Login with username&password")
        name = input('Enter a name:')
        password = input('Enter a password:')
        if name in a.keys() and password in a.values():
            print("Login Successfully")
        else:
            forgot = input('forgot your password y/n:')
            if forgot == 'y':
                new = input("Enter your new password:")
                a[name] = new
                if name in a.keys():
                    name = input("Enter your name:")
                    password = input("Enter your password:")
                    if a[name] == password:
                        print("password changed successfully")

                print(a)
            else:
                newuser = int(input("1 Create a new account:  2 Existing user: 3 Exit:"))

                if newuser == 1:
                    x.newuser()

                if newuser == 2:
                    x.existinguser()

                if newuser == 3:
                    print("exit")


x = login()

newuser = int(input("1 Create a new account:  2 Existing user: 3 Exit:"))

if newuser == 1:
    x.newuser()

if newuser == 2:
    x.existinguser()

if newuser == 3:
    print("exit")
