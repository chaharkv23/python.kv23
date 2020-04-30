with open('program5.py') as f:
    for i in f:
        if(i[0]!='#'):
            print(i,end="")