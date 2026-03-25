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