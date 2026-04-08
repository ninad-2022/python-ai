# # Duck Typing 
# Duck = quack  

# Java 
#     - a bird is considered a duck only if it is born as a duck from duck egg 

# void print(Employee emp){
#     System.println(emp.login())
# }

# print(new Employee())
# print(new Customer())//invalid type 


# Python  
#     - anything which walks like a duck and says quack is considered as a duck 
#     human 
#     robot 
 

# def sing(bird):
#     bird.quack()

def printName(obj):
    print(obj.getName())

class Employee:

    def __init__(self, name,salary, city):
        self.name = name 
        self.salary = salary
        self.city = city 

    def getName(self):
        return self.name

emp = Employee("AAA",123,"Pune")
printName(emp)

class Customer:

    def getName(self):
        return "customername"
 

cust = Customer()
printName(cust)