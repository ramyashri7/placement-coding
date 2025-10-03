n=input().strip()
if int(n)>0:
    print(int(n[0])+int(n[-1]))
else:
    a=abs(int(n))
    p=str(a)

    print((int(p[0]))+(int(p[-1])))
