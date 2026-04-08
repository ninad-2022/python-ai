# method overloading: two methods with same name in same class with different parameters

# print(10+20)#30

# a = "abc"

# print("10" + a)#10abcd

 

# print(len([10,20,30]))

# print(len((1,2,3,4)))

 

class Arithmetic:

    def add(self,a,b):

        return a+b

 

    def add(self,a,b,c):

        return a+b+c

 

calc = Arithmetic()

 

print(calc.add(10,20))

print(calc.add(10,20,30))

 

# city = "Pune"

# city = "Mumbai"

# print(city)#Mumbai