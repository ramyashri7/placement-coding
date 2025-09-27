num,n=map(str,input().split())
count=0
for i in num:
    
    if(i==n):
        count=count+1
    else:
        continue
print(count)
