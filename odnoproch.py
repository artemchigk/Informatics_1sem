a=input().split()
for i in range (len(a)//2):
    s=a[i*2]
    ss=a[i*2+1]
    a[i*2]=ss
    a[i*2+1]=s
print(a)
