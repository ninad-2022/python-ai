# 3.3-dot-product.py

import numpy as np

a = np.array([10,20,30])
b = np.array([1,2,3])

# element wise multiplication 
print(a * 2)
print(a * b)

# matrix multiplication 
# dot product 
print(np.dot(a,b))
print(a@b) #python version 3.5

# number of colums of first matrix must equal number of rows of second matrix 
# shape of results matrxi wil be equals to the number of rows of first coumns of second matrix



x = np.array([
    [1,2],
    [3,4]
])

y = np.array([
    [5,6],
    [7,8]
])

print(x @ y)