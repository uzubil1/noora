class Student:
    pass
    def __init__(self, name, ID, credits, gpa):
        self.name = name
        self.id = ID
        self.credits = credits
        self.gpa = gpa

def print_student(student):
    print(f"Student: {student.id}, {student.name}, {student.credits}, {student.gpa}")

def main():
    student1 = Student("Youssef",345678, 13, 3.7)
    student2 = Student("Safia", 234567, 17, 3.5)
    student3 = Student("Saad", 2345987, 12, 4.0)
    
    print_student(student1)
    print_student(student2)
    print_student(student3)

if __name__ == "__main__":
    main()
