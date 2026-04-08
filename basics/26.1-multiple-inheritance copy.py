# Object classs (base for all classes )

class Animal:
    def __init__(self, age, weight, height, color, breed):
        self.age= age
        self.height= height
        self.weight= weight
        self.color= color
        self.breed= breed

    def profile(self):
        print(f"age: {self.age}")
        print(f"weight: {self.weight}")
        print(f"height: {self.height}")
        print(f"color: {self.color}")
        print(f"breed: {self.breed}")

class Pet(Animal):
    def __init__(self, name, price, legal, age, weight, height, color, breed):
        super().__init__(age, weight, height, color, breed)
        self.name=name
        self.price=price
        self.legal=legal


class Horse(Pet):
    def profile(self):
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"Is Legal: {self.legal}")
        print(f"age: {self.age}")
        print(f"weight: {self.weight}")
        print(f"height: {self.height}")
        print(f"color: {self.color}")
        print(f"breed: {self.breed}")
    
h = Horse("AA", 10000, "yes", 12, 42, 234, "red", "lab")
h.profile()