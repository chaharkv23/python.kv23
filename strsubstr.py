s=input()
sub=input()
c=0
d=len(sub)
for i in range(len(s)):
	if s[i] == sub[0]:
		if s[i:(d+i)] == sub:
			c+=1
print(c)
