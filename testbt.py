def writefile(filename):
    f=open(filename,'w')
    for i in range(2):
        s,s1,s2,t,g=input().split()
        t=int(t)
        f.write('%s %20s %10s %5d %10s\n'%(s,s1,s2,t,g))
    f.close()
def readfile(filename):
    f=open(filename,'r')
    for line in f:
        print(line,end='')
    f.close
filename='output.txt'
readfile(filename)