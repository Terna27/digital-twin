

class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        return f"my car is a {self.brand} {self.model} {self.year} model"
        
        
        

def run():
     new_car1 = Car("Toyota", "Corolla", 2020)
     new_car2 = Car("Honda", "Civic", 2022)
     
     result1 = new_car1.display_info()
     result2 = new_car2.display_info()
     
     print(result1)
     print(result2)
     