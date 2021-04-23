name = ['kiran', 'vignesh','udaya','mani']
l = 'laxmanan'
num = [101,102.103,104,105,106]
print(name[1])
print(len(name))
print('kiran' in name)
print(l.upper())
print(l.lower())
print(l.strip())
print(l.replace('l','m'))
print(l.split(","))
print(max(num))
print(sum(num))
m = 'vign'
data = "my\"name\"is\n{}"
print("my name is {}".format(m))

print(data.format(m))
for record in name:
    if record =='udaya':
      print('record found')
print(l[:5])
print(l[2:6])
print(l[5:])
print(l[-2:-1])




