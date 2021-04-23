import datetime
from numpy import random
print("happy journey")
current_date_time = datetime.datetime.now()
print("DATE & TIME:", current_date_time)
train_no = random.randint(9,size=(4))
print('Train no:', train_no)

a = {'chengalpattu': 1, 'paranur': 2, 'singaperumal': 3, 'kovil': 4, 'maraimalai nagar': 5, 'kattangulattur': 6,
        'potheri': 7, 'guduvancheri': 8, 'Urappakkam': 9, 'Vandalur': 10, 'Perungulattur': 11, 'tambaram': 12,  'Chrompet': 13,
        'pallavarm': 14, 'tirusulam': 15, 'minambakkam': 16, 'palavanthangal': 17, 'st Thomas Mount': 18,
        'guindy': 19, 'saidapet': 20, 'mambalam': 21, 'kodambakkam': 22, 'nungambakkam': 23, 'chetpet': 24,
        'egmore': 25, 'park': 26, 'fort': 27, 'Marina beach': 28}

s =input('Enter your starting point:')
d =input('Enter your destination:')
i = a[s]
j = a[d]
x = j - i
cost=5
if x < 10:
        print(cost)
elif x >= 10 and x < 20:
        c = cost+5
        print(c)
else:
        c = cost+10
        print(c)
