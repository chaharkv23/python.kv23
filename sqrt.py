import math
c=50
h=30
d=list(map(int,input().split(',')))
for i in d:
    q=(2*c*i)/h
    sq=math.sqrt(q)
    print(round(sq))
