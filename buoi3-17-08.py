def PayWork(h,r):
    if h>40:
        p=40*r + (h-40) * r*(1.5)
    else:
        p=h*r
    p=float(p)
    print('Pay:',p)
