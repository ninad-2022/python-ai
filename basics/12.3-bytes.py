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

print("-"*10, "slicing", "-"*10)
a = b'ABCDEFG'
print(a[0:])
print(a[3:])
print(a[4:])
print(a[2:5])

print("-"*20)
b = bytearray([65,66,67,68,69,70])
print(b)
print(b[0:])
print(b[3:]) #str[start:stop:step]
print(b[3:5])

b[0] = 90
print(b)
# above will create separate data values for each slicing and
# it will be stored in separate memory and this will utliize extra memory

print("-"*20)
mv = memoryview(b)
print(mv[2:])
print(mv[2:].tobytes())
print(mv[2:])
mv[1:4]= b"XYZ"

print(mv)
print(b) #modified

data = b"Topper"
mv2 = memoryview(data)
print(mv2[0])
print(mv2[1])