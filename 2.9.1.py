with open ('2.9.txt','r') as txtfile:
    a=txtfile.readlines()
a=a[0]
b=a.split('.')
print(b)
d=a.split('!')
print(d)
e=a.split('?')
k=a.count('...')
print(k)
print(e)
summ=len(b)+len(e)+len(d)-3-k
print(summ)