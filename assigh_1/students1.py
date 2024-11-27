class Student:
    pass
    def __init__(self, name='Student', ID='No ID', credits=0, gpa=0.0):
        self.name = name      # Default: 'Student'
        self.id = ID          # Default: 'No ID'
        self.credits = credits  # Default: 0
        self.gpa = gpa        # Default: 0.0

def print_student(student):
    print(f"Student: {student.id}, {student.name}, {student.credits}, {student.gpa}")

def main():
    student1 = Student("Youssef", 345678, 13, 3.7)  # Custom values for student1
    student2 = Student()  # Using default values for student2 (no arguments)
    
    print_student(student1)  # Print student1 with custom values
    print_student(student2)  # Print student2 with default values

if __name__ == "__main__":
    main()
