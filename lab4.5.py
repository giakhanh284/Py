def tableDraw(i,s):
    if i <10:
        if s<10:
            print("| %d|  %d|"%(i,s))
            print("--------")
        else:
            print("| %d| %d|"%(i,s))
            print("--------")
    else:
        if s<100:
            print("|%d| %d|"%(i,s))
            print("--------")
        else:
            print("|%d|%d|"%(i,s))
            print("--------")
n=int(input())
print("|i |sum|")
print("--------")
s=0
for i in range(1,n+1):
    s+=i
    tableDraw(i,s)