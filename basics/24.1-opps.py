import random

class Employee:
    # classs methods
    company = "Topper Skills"
    # instance methods
    def __init__(self, id , name, sal):
        self.id = id
        self.name = name
        self.salary = sal
    
    # isinstance method 
    def printProfile(self):
        print(f"Emp id {self.id}")
        print(f"Name {self.name}")
        print(f"Salary id {self.salary}")
    

    @staticmethod
    def getCompany():
        return Employee.company

    @staticmethod
    def generatePassword():
        return f"{random.random()}"
    
    @classmethod
    def createEmployee(cls):
        # return { "empId": id, "name":name, "salary": sal }
        print(cls.generatePassword())

print(Employee.getCompany())
print(Employee.createEmployee())