# bytes datatypes 
# low level or hardware close work should be done in byte to optimizd the performance

a = b"bcbcd"
b=bytes([65])

print("a:",a)
print(type(a))

print(type(b))
c = "मराठी".encode("utf-8")
#c = "ABC".encode("utf-8")
print("c:",c)

# ASCII (english alphabates, digits, basic symbols = total <=128 )
# 3 bytes per character in marathi 
x =b'\xe0\xa4\xe0\xb0\xa4\xe0\xa5'
print("x:",x)
print(type(x))

# bytes to string 
ss = c.decode("utf-8")
print("ss",ss)
print(type(ss))

# bytes is immutable
d = "hello" 
print("d[0]:",d[0])

print("-"*10, "bytesarray()", "-"*10)
name = bytearray([65,66,77])
# name[0]=90
print("name", name)
name.append(84) #add an element at the end
print("name:append", name)
name.extend([84,90,65]) #add en element at the end
print("name:extend", name)
name.reverse()
print("name: reverse", name)