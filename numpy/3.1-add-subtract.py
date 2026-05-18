import numpy as np;

print("***********Arithmatic Operation********")
a = np.array([1,2,3,4,5])
print("a:",a)

a = a + 2
print("a + 2:",a)

a = a * 2
print("a * 2:",a)

a = a / 2
print("a / 2:",a)

a = a**2
print("exponential:",a)

# basic difference 
# scaler: single Value
# vector: multiple value 


c = np.array([10,20,30,40,50,60])
b = np.array([1,2,3,4,5,6])

# a + b 
# 10 + 1
# 20 + 2 

print("b - c:", b - c)
print("b + c:", b + c)
print("b/c):", b/c)
print("b//4:", b//4) # floor division
print("b/4):", b/4) # division
print("b*c):", b*c)

# modulus
print(b%4)