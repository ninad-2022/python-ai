# Function annotations:-
#   - it defines the datatype suggestions for function parameters and return value
#   - it does not make it mandatory to follow to given dataTypes

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
print(add("10", "20"))
