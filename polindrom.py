a=str(input())
polindrom=1
Zpolindrom=1
print(len(a))
for i in range (len(a)):
    print(a[i])
    print(a[-i-1])
    if a[i]!=a[-1-i]:
      polindrom=0
      break
a=a.replace('E','3')
a=a.replace('J','L')
a=a.replace('S','2')
a=a.replace('Z','5')
print(a)
for i in range (len(a)):
    if a[i]!=a[-1-i]:
        Zpolindrom=0
        break
if polindrom==1 and Zpolindrom==1:
    print(a+" is a mirrored polindrom")
if polindrom==0 and Zpolindrom==1:
    print(a+" is a mirrored string")
if polindrom==1 and Zpolindrom==0:
    print(a+" is a regular polindrom")
if polindrom==0 and Zpolindrom==0:
    print(a+" is not a polindrome")      
