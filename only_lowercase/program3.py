with open('lower.txt','r') as f:
    with open('lower3.txt', 'w') as f2:
        for i in f:
            if(i[0].islower()==True):
                f2.write(i)



