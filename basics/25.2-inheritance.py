# class Dog:
#     def __init__(self, age, color, weight, speed):
#         self.age= age
#         self.color= color
#         self.weight= weight
#         self.speed= speed

#     def running():
#         print(f"runing at {self.speed}")
    
#     def color():
#         print(f"runing at {self.color}")


# class Horse:
#     def __init__(self, age, color, weight, speed):
#         self.age= age
#         self.color= color
#         self.weight= weight
#         self.speed= speed

#     def running():
#         print(f"runing at {self.speed}")
    
#     def color():
#         print(f"runing at {self.color}")

# instead of two different classes we should make a single class named Animal

class Animal:
    def __init__(self, age, color, weight, speed):
        self.age= age
        self.color= color
        self.weight= weight
        self.speed= speed

    def running(self):
        print(f"runing at {self.speed}")
    
    def eating():
        print(f"eating...")

    def details(self):
        print(f"Color: {self.color}")
        print(f"age: {self.age}")
        print(f"weight: {self.weight}")
        print(f"speed: {self.speed}")

class Horse(Animal):
    pass

class Horse(Animal):
    def __init__(self, name, age, color, weight, speed):
        super().__init__(age,color, weight, speed)
        self.name = name

    def barking(self):
        print(f"{self.name} barking...")
    

h1 = Horse("strom", 12, "red", 15, 34)
print(h1.barking())