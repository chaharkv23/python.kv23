def fib(n):
    a=0
    b=1
    if(n==1 or n==0):
        print(a)
    elif(n<0):
        print("enter a value except negative")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if(c<100):
                print(c)
fib(100)