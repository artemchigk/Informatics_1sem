a=input().split()
d=0
c=0
for i in range (len(a)):
    if a.count(a[i])>c:
        d=a[i]
print(d)