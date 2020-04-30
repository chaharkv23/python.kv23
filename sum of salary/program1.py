s = 0
with open("salary.txt","r") as f:
    w = f.readlines()
    for i in w:
        s+=int(i)
print(s)
