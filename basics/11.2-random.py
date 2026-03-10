import random

print("*" *10, "random.random()", "*"*10)

print(random.random())

print("*" *10, "random.radint()", "*"*10)
print(random.randint(1000,9999))

print("*" *10, "random.randrange()", "*"*10)
print(random.randrange(1,100))
print(random.randrange(1,100,2))
print(random.randrange(0,100,2))

print("*" *10, "random.choice()", "*"*10)
name="Topper Skills"
print(random.choice(name))

cities=["pune", "mumbai", "nashik", "nagpur", "satara", "sangli", "beed"]
print(random.choice(cities))
print(cities)

nums = [10,20,30,40,50,60,70,80,90]
print(nums)
print(random.shuffle(nums))
print(nums)

print(random.shuffle(cities))


