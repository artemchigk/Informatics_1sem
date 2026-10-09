N=int(input())
a=input().split()
f=0
for i in range (N):
    a[i]=int(a[i])
min=min(a)
for i in range (max(a)-min):
    if min in a:
        f=f+a.count(min)
        #print(f)
    if f== (N+1)//2:
        break 
    min=min+1
print(min)
