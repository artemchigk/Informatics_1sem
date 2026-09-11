N=str(input())
Nr=N[::-1]
b=int(input())
c=int(input())
#print(len(N))
summ=0
spisok=''
lenn=0
for i in range (len(N)):
    summ=summ+int(Nr[i])*(b**i)
#print(summ)
summ1=summ
while summ1!=0:
    lenn=lenn+1
    summ1=summ1//c
#print(lenn)
while lenn!=0:
    spisok=spisok+str(summ-summ//c*c)
    summ=summ//7
    lenn=lenn-1
#print(spisok)
spisok=spisok[::-1]
print(spisok)
