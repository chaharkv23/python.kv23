import math
f=1

a=list(map(int, input("enter numbers").split(',')))
for i in a:
	f=math.factorial(i)
	print(f,end=',')

