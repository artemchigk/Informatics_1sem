f=open('input1.txt', 'r')
h=[]
for line in f:
    h=h+[line]
N=str(h[0]).split()
#print(N)
b=int(h[1])
c=str(h[2])
#print(N)
Nr=N[::-1]
#print(len(N))
#print(type (N))
summ=0
if c=='+':
    summ1=0
if c=='-':
    summ1=0
if c=='*':
    summ1=1
lenn=0
spisok=''
for i in range (len(N)):
    t=N[i]
    tr=t[::-1]
    #print(tr)
    for k in range (len(t)):
        summ=summ+(int(tr[k]))*(b**k)
    #print(summ)
    if c=='+' or c=='-':
        summ1=summ1+summ
        summ=0
    if c=='*':
        summ1=summ1*summ
        summ=0
#print(summ1)
summ2=summ1
while summ2!=0:
    lenn=lenn+1
    summ2=summ2//b
#print(lenn)
while lenn!=0:
    #print(summ1)
    spisok=spisok+str(summ1-summ1//b*b)
    summ1=summ1//b
    lenn=lenn-1
#print(spisok)
spisok=spisok[::-1]
#print(spisok)
g=open('output1.txt', 'w')
g.write(str(spisok))
g.close
f.close