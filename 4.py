f=open('input.txt', 'r')
h=0
a=[]
for line in f:
    a=a+[line]
b=a[0]
c=a[1]
b=b.split()
if c=='+':
    while len (b)!=0:
        h=h+int(b[0])
        b.pop(0)
if c=='-':
    while len (b)!=0:
        h=h-int(b[0])
        b.pop(0)
if c=='*':
    while len (b)!=0:
        h=h*int(b[0])
        b.pop(0)
g=open('output.txt', 'w')
g.write(str(h))
g.close
f.close