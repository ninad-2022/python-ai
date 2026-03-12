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
