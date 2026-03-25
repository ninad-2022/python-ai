# packing 
packing = 1,2,3,4,5
print(packing)

# unpacking 
[a,b,c] = [1,2,3]
print(a)
print(b)
print(c)

# _: ignore values 
# *restr: * use for rest
x, _, *restr = [1,2,3,66]
print(x)
print(restr)
print(_)

# Unpacking dictionaries
data = {"name": "ninad", "age":13}
print(data["name"])