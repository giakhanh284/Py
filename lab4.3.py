def Factors(n):
    print("%d*"%n,end='')
    if n%2==0:
        for i in range(int(n/2),1,-1):
            if n%i==0:
                print("%d*"%i,end='')
    else:
        for i in range(int(n/3),1,-1):
            if n%i==0:
                print("%d*"%i,end='')
    print(1)
Factors(2)