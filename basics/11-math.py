import math


print(math.factorial(4))


print(0.3 == 0.3)
print(0.1 + 0.2) #0.3333
print(math.isclose(0.1+0.2, 0.3)) #to compare the floating number
print(0.1+0.2, 0.3)
print(math.isclose(0.3, 0.3))

# math.floor() rounds towards negative infinity (always down to the next smaller integer).
# math.trunc() rounds towards zero (simply cuts off the decimal part).
print(math.floor(123.29))
print(math.floor(-123.29))

print("----------math.truc()-----------")
print(math.trunc(128.19))
print(math.trunc(-4.5))

print(math.factorial(4)) #4*3*2*1
print(math.factorial(5))
print(math.factorial(10))

print("----------math.sqrt------------")
print(math.sqrt(16))
print(math.sqrt(25))
print(math.sqrt(36))

print("-----gretest common divisor-----")
print(math.gcd(12,9))
print(math.gcd(10,5))
print(math.gcd(20,18))

print("-----least common divisor-----")
print(math.gcd(12,9))
print(math.gcd(10,5))
print(math.gcd(20,18))

print("-----least common multiple-----")
print(math.lcm(9,6))
print(math.lcm(4,3))
print(math.lcm(10,15))