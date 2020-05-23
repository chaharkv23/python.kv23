import numpy as np
R = int(input("Enter the number of rows:"))
C = R
s=0
d=0
print("Enter the entries in a single line (separated by space): ")
lst = list(map(int, input().split()))
matrix = np.array(lst).reshape(R, C)
for i in range(R):
    for j in range(R):
        if(i==j):
            s+=matrix[i][j]
        if((i+j)==(R-1)):
            d+=matrix[i][j]
print(abs(s-d))



