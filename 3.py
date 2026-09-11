a=input().split()
b= len (a)
c=0
while len (a)!=0:
    c=c+int(a[0])
    a.pop(0)
print(c/b)

