n = ['avi',]
p = ['123',]

newuser = int(input("1 Create a new account or 2 Existing user"))

if newuser == 1:
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
                        print("Please Login again")
                print(a)
            else:
                print("Please Login again")

else:
    a = dict(zip(n, p))
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
            print("Please Login again")