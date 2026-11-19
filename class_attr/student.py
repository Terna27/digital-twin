

class Student:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def has_passed(self):
        return self.score >= 50
    
    def deisplay_result(self):
        
        if self.has_passed():
            print(f"{self.name} Passed")
        else:
            print(f"{self.name} Failed")
            
            
def run():
    result = Student("Terna", 9)
    
    result.deisplay_result()
   