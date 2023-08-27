import math
def giaiThua(k):
    if k==0:
        return 1
    else:
        s=1
        for i in range(1,k+1):
            s=s*i
        return s
def Estimate_pi():
    k=0
    p=0
    t=((2*math.sqrt(2))/9801)
    while(True):
        d=((giaiThua(4*k)*(1103+26390*k)))/((giaiThua(k)**4)*((396**(4*k))))
        p=p+((giaiThua(4*k)*(1103+26390*k)))/((giaiThua(k)**4)*((396**(4*k))))
        if abs(d*t) < 1e-15:
            break;
        k+=1
    return 1/(p*t)
print(Estimate_pi())