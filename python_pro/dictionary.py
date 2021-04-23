create_list = [i for i in range(10,20)]
print(create_list)
even_number = [i for i in range (11,30)if i % 4 == 0]
print(even_number)
even = [i if i % 6 != 0 else "odd" for i in range(10,20)]
print(even)

create_dict = {i:"number" for i in range(10,20)}
print(create_dict)
even = {i: "number" for i in range(10,200) if i % 2 == 0}
print(even)

even_odd = {i: "even" if i % 4 == 0 else "odd" for i in range(10,20)}
print(even_odd)

#dictionary uing odd or even
n = int(input("enter the no:"))
a = {i: 'odd' if i % 2 != 0 else 'even' for i in  range(1,n)}
print(a)
print(a.keys())
print(a.values())

















