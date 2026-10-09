n=int(input())
def f(a):
    from math import log2
    b=a
    g=[]
    for k in range (int(log2(a))+1):
        for i in range (int(a)):
            if b%(i+2)==0.0:
                print(i+2)
                g=g+[str(i+2)]
                b=b//(i+2)
                break
    return g
print(f(n))