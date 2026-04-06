# Object Oriented Programming Model 
#     - Object Oriented Programming (OOP) is a programming paradigm that uses objects and 
# classes to structure software design. 
# It focuses on creating reusable and modular code by organizing data and behavior into objects.
 
# logic = data + operation

# Class 
# Object 
# Inheritance 
# Polymorphism 
# Encapsulation 
# Abstraction

# class = category 
# class is model 
# model/bluprint = representation
# object or class 
# row houses =  model 
# objects  = class (state , behaviour)
# bricks = ? 
# class is a model of an object 
# class defines state (data) and behaviour(activities) of the objects 
# Syntax 
#     class ClassName:
#         body

# object is an instance of a class 
# object has state and behaviour 
# state = data related to the object 
# behaviour = activities of the object 
# Ex: 
# Dog 
#     state = color,age,weight 
#     behaviour = barking,eating,running 
#     class uses properties to define the state of the objects 
#     class uses methods to define behaviour of the objects.

class Dog:
    def __init__(self, name,color):
        self.color = color
        self.name = name 

    def barking(self):
        print(f"{self.name} is barking")

    def running(self):
        print(f"{self.color} is running")
    
    def eating(self):
        print(f"{self.name} is eating")

dog1 = Dog("Tommy", "White")
dog2 = Dog("Gabaru", "Black")


dog1.barking()
dog1.running()
dog1.eating()

print("-"*20)

dog2.barking()
dog2.running()
dog2.eating()