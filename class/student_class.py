


class Student:
    
    def __init__(self, name, score):
        
        self.name = name
        self.score = score 
        
    def score_board(self):
        return (f"{self.name} scored {self.score}% in the exams")
    
def run():
    
    result = Student(input("name : "), input("score : "))

    final = result.score_board()
    print(final)
    