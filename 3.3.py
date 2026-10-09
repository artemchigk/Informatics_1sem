a=input().split()
p1=int(a[0])
p2=int(a[1])
t1=0
t2=0
def f(a):

    from math import log2
    b=a
    g=[]
    for k in range (int(log2(a))+1):
        for i in range (int(a)):
            if b%(i+2)==0.0:
                g=g+[str(i+2)]
                b=b//(i+2)
                break
    return g
h1=f(p1)
h2=f(p2)
j=[i for i in h1 if i in h2]
if j==[]:
    j=['1']
for i in range (len(j)):
    j[i]=int(j[i])
mini=min(j)
for i in range (100):
    if t1*p1-t2*p2==mini:
        break
    if t1*p1-t2*p2<mini:
        t1=t1+1
    else:
        t2=t2+1
i1=0
i2=1
for i in range (100):
    if -i1*p1+i2*p2==mini:
        break
    if -i1*p1+i2*p2<mini:
        i2=i2+1
    else:
        i1=i1+1
t2=-t2
if abs(t1)+abs(t2)>abs(i1)+abs(i2):
    t1=-i1
    t2=i2
print(t1, t2, mini )
    