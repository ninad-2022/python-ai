def add (a, b):
    return a + b
print(add(1,2))

addv2 = lambda a, b: a+b
print(addv2(1,4))

cities = ["mumbai", "pune", "nagpur"]

val = map(lambda city:(city , len(city)), cities)
print(list(val))