#5.1
def ShowData(filename):
    f=open(filename,'r')
    for line in f:
        print(line)
#5.2       
def stats(filename):
    f=open(filename,'r')
    longets=''
    for line in f:
        if len(line)  > len(longets):
            longets=line
    print('The longest line is = ',len(longets))
    print(longets)
    f.close()
#5.3   
def StatsCount(filename):
    f=open(filename,'r')
    i=0
    for line in f:
        if line !='\n':
            i+=1
    print('Line Count:',i)
    f.close()
#5.4   
def StatsContain(filename):
    f=open(filename,'r')
    for line in f:
        if line.find('file') != -1 or line.find('File') != -1:
            print(line,end='')
    f.close()
#5.5    
def CallUpper(filename,pattern):
    f=open(filename,'r')
    for line in f:
        line=line.replace(pattern,pattern.upper())
        print(line)
    f.close()