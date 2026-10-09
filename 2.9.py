with open ('2.9.txt','r') as txtfile:
    a=txtfile.readlines()
a=a[0]
b=''
c=''
d=''
print(a)
a=a.split('.')
for i in range (len(a)):
    b=b+' '+a[i]
print(b)
b=b.split('!')
for i in range (len(b)):
    c=c+' '+c[i]
print(a)
a=a.split('?')
for i in range (len(c)):
    d=d+' '+d[i]
print(a)
print(len(a))