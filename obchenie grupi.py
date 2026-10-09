a=input().split()
b=int(a[0])
g=''
c=a[1]
for i in range (len(c)//b):
    z=c[i*b: (i+1)*b]
    f=z[::-1]
    g=g+str(f)
print(g)

