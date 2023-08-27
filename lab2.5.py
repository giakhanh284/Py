s=input("String ")
c=input("Letter ")
s1=input("Word ")
n=s.count(c)
k=s.count(s1)
str1="There are %d \'%s\' but only %d %s in %s"
print("There are {} '{}'s but only {} {} in {}".format(n,c,k,s1,s))