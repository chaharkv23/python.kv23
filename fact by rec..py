def factrec(n):
    if(n==0):
        return 1
    return n*factrec(n-1)
x = 10
res = factrec(x)
print(res)