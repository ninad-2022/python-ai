import numpy as np;

a = np.array([10,20,30,40,50,60])
print("a:", a)

# check datatype 
print("sataType:",a.dtype)

# indexing 
# print(a[0])
# print(a[-1])

# array[index, index, index] 
# print(a[[0, 2, 5]])

# boolean indexing 
print(a[a < 20])

# 2d array 

b = np.array([
    [1,2,3],
    [4,5,6],
    [7,6,8],
])
print("*********************")
print(b[0][0])
print(b[1][2])
print(b[0][0])
print(b[2][1])