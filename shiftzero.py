a=[]
b=[]
n=list(map(int,input("enter number")))
for i in n:
    if (i==0):
        a.append(i)
    else:
        b.append(i)
print(*(b+a))   
