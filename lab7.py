'''def nested_sum(a):
    s=0
    l=[]
    for i in range(len(a)):
        l.extend(a[i])
    for i in range(len(l)):
        s+=int(l[i])
    return s
t=[[1,2,3],[3],[4,5,6]]
print(nested_sum(t))'''
'''def cumsum(a):
    for i in range(1,len(a)):
        a[i]=(a[i]+a[i-1])
    return a
t=[1,2,3]
print(cumsum(t))'''
'''def middle(a):
    a.pop(0)
    a.pop(len(a)-1)
    return a
t = [8, 9, 5, 2, 10]
res = middle(t)
print(res)'''
'''def is_sorted(a):
    l=a
    l=sorted(l)
    if l==a:
        return True
    else:
        return False
t = ['a', 'b', '1', '3']
res = is_sorted(t)
print(res)'''
'''def in_bisect(fname,key):
    f=open('fname','r')
    for line in f:
        if line.find(key) != -1:
            return True
    f.close()
    return False'''
