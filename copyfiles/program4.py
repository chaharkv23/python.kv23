with open('copy1.txt','r') as f1:
    with open('copy2.txt','w') as f2:
        for i in f1:
            f2.write(i)