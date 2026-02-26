# variable: it is a reference which refers to the object store in the heap memory.
# variable cannot be declaraed without assigning a value.
import sys

city="Pune"
print(city)

PI=3.14
print(PI)
PI="somethign else"
print(PI)

major=None
print("majorm",major)

print("size",sys.getsizeof(city))