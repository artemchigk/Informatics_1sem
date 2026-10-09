with open ('2.10.txt', 'r', encoding="UTF-8") as  f:
    text = f.read()
    l=0
glass=['у','е','ы','а','о','э','я','и','ю']
a=text.split()
print(a)
b=a
for i in range (len(a)):
    str=a[i]
    b=str
    print(str)
    for k in range (len(str)):
        lastglass=str[k]
        if str[k] in glass:
            l=l+1
            if l>0:
                b[i]=str[k]+'с'+lastglass
print(b)

