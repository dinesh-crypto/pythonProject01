a = [5,2,8,7,1]
temp = 0
print("element of original array")
for i in range(0,len(a)):
 print(a[i])

 #sorting the array
 # 1 2 5 7 8
 # 4 3 2 1 0
 # -5 -4 -3 -2 -1

for i in range(0,len(a)):
   for j in range(i+1,len(a)):
       if a[i]>a[j]:
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        print()


print("second element of original array")
for i in range(0,len(a)):
 b=int(input("enter the value:"))
 print(a[b])
 break

