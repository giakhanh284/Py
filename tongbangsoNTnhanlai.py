import math
def PrimeFactors(n):
    while n%2==0:
        print("%d*"%2,end='')
        n/=2
    for i in range(3,int(n/2),2):
        while(n%i==0):
            n/=i
            if n>2:
                print("%d*"%i,end='')
            else:
                print(i,end='')
    if(n>2):
        print(int(n))
PrimeFactors(40)        