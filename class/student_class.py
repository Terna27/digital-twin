
name = input("Enter your name : ")
score = input("Enter your score : ")

class Student:
    
    def __init__(self, name, score):
        
        self.name = name
        self.score = score 
        
    
    def score_board(self):
        return (f"{self.name} scored {self.score}% in the exams")
        
    def update_score(self, new_score):
            self.score = new_score
            return self.score_board()
    
def run():
    
    result = Student(name, int(score))

    if result.score < 50:
        print("Failed")
        
        new = int(input("Enter a new score : "))
        
        result.update_score(new)
        
        final = result.score_board()
        print(final)
        
    else:
        final = result.score_board()
        print(final)
    