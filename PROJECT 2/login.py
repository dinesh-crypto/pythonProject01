otp = 4335
n = ['avi',]
p = ['123',]
a=0
no = int(input('enter a no:'))
while a < no:
    name = input('Enter a name:')
    password = input('Enter a password:')
    if name in n:
        print('Already existed')
    else:
        n.append(name)
        p.append(password)
        no -=1
        print("Created successfully")
        print(n)
        print(p)

a = dict(zip(n,p))
print(a)
print(a.values())
print(a.keys())

login = input('Do you want to login yes/no:')
if login == 'yes':
    username = input('Enter your name:')
    userpas = input('Enter your password')
    if username in a.keys() and userpas in a.values():
        print('Successfully logged in')
    else:
        print('does not match.enter your username and password correctly')

forgot = input('forgot your password yes/no:')
if forgot == 'yes':
    print("your otp is:")
    print(otp)
    phone = int(input('enter your otp:'))
    if otp == phone:
        new = input("Enter your new password:")
        a[username] = new
        if username in a.keys():
            username = input("Enter your name:")
            password = input("Enter your password:")
            if a[username] == password:
                print("password changed successfully")
        print(a)

else:
    print("Accounts created successfully")
    print(a)

