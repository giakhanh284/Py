def xoaPhanTu(a,k):
    if a[0] - a[1] !=0 and a[1] - a[2] ==0:
        return 1
    if a[k-1] - a[k-2] != 0 and a[k-2] - a[k-3] ==0:
        return k 
    for i in range(1,k-1):
        if a[0] - a[i] != 0:
            return i+1        
t=int(input())
b=[]
for i in range(t):
    k=int(input())
    a=list(map(int, input().split()))
for i in range(t):
    print(b[i])