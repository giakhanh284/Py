def StatsCount(filename):
    f=open(filename,'r')
    '''i=0
    for line in f:
        i+=1
        if line.find('the') == -1:
            print(i)'''
    '''i=0
    for line in f:
        i+=1
    print(i)'''
    out=open('output.txt','w')
    for line in f:
        if line[0] == line[0].upper():
            out.write(line)
    out.close()
    f.close()
    out=open('output.txt','r')
    for line1 in out:
        print(line1,end='')
    out.close()
filename='testfile.txt'
StatsCount(filename)
