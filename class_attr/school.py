
class Student:
    
    school = "Greenfield"
    school2 = "TN MACUALEY"
    
    def __init__(self, name):
        self.name = name
    
def run():
    stud1 = Student(input("Enter name : "))
    stud2 = Student("Mary")
  
    print(f" {stud1.name} is from {stud1.school2} Academy")
    # print(Student.school)