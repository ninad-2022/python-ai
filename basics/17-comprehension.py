# []: comprehension is use to write a single line of the code in one line for the repeatable 

nums = []

for i in range(10):
    nums.append(i+2)
print(nums)

# syntax: expression and loop 
nums = [n+2 for n in range(10)]
print(nums)

# with condition 
# [expression for item in interable condition]
even = [n for n in range(10) if n % 2==0]
print(even)


oddEven= ["zero" if n ==0 else 
            "even" if n % 2==0 else 
                                     "odd" 
          for n in range(10)]
print(oddEven)


y = 1
if y == 0:
    print(y)

# comprehension for dictory
# value will came from this "i*i for i in range(20) if i >0" and get assign into the i 
xx = {i: i*i for i in range(20) if i >0}
print(xx)

# create dic of city with no of character in the name

cities =["mumbai", "pune", "nagpur", "raigad"]
count = { city: len(city) for city in cities}
print(cities)
print(count)

# create dictory from two list 
places = ["vashi", "ghansoli", "panvel"]
pincode = [1910, 2434, 35445, 43534]
# zip is used to combine tuple list 
locations = { k:v for k, v in zip(places, pincode)}
print(locations)