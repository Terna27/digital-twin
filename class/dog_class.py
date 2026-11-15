

class Dog:
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        return (f"{self.name} says woof!")
    
    
def run():
    dog1 = Dog("Lucky", "chiwawa", 3)
    
    result = dog1.bark()
    print(result)