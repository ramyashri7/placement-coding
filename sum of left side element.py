n=int(input())
a=list(map(int,input().split()))
c=0
print(c,end=" ")
for i in range(1,n):
    c=c+a[i-1]
    print(c,end=" ")
