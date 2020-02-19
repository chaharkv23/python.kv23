t=(1,2,3,6,9,21)
t1=int(input())
for i in t:
	if t.count(i):
		if t1 in t:
			print('present')
			break
		else:
			print('not present')
			break
