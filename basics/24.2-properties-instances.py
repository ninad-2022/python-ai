# Class properties → shared by all objects
# Instance properties → unique to each object

class Employee:
    # class properties 
    company = "Topper Skills"
    def __init__(self, id, name, sal):
        # instance properties 
        self.empId = id
        self.name = name
        self.salary = sal


emp1 = Employee(11, "Ninad", "12LPA")

print(f"Company:", emp1.company)
print(f"name:", emp1.name)
print(f"salary:", emp1.salary)