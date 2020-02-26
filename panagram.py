s=input()
a=s.lower()
for i in range(97,123):
    if chr(i) not in a:
        print("not panagram")
        break
else:
        print("panagram")
