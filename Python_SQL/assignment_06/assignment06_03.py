class student:
    def __init__(self, rollno, studentname, course, marks):
        self.rollno = rollno
        self.studentname = studentname
        self.course = course
        self.marks = marks

    def __str__(self):
        return (f"Roll no : {self.rollno}, Student Name : {self.studentname}, Course : {self.course}, Marks : {self.marks}")

    def accept_data(self):
        self.rollno = input("Enter Roll no : ")
        self.studentname = input("Enter Student Name : ")
        self.course = input("Enter Course Name : ")
        self.marks = {}
        for _ in range (5):
            subject = input("Enter the Subject Name : ")
            marks = int(input(f"Enter the Marks for {subject} : "))
            self.marks[subject] = marks

    def print_data(self):
        print(self)

#  accept record
students = []
for i in range(5):
    print(f"Enter the Student Details : {i + 1} : ")
    student_obj = student(None, None, None, None)
    student_obj.accept_data()
    students.append(student_obj)

print(f"Student Records : ")
for student in students:
    student.print_data()