"""The marks obtained by a student in 3 different subjects are input by the user.
Your program should calculate the average of subjects and display the grade. The
student gets a grade as per the following
rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59
F """

s1 = float(input("Enter the marks of the first subject : "))
s2 = float(input("Enter the Marks of Second Subject : "))
s3 = float(input("Enter the marks of third subject : "))

avg = (s1 + s2 + s3) / 3
print(f"Average Score of the Student is {avg}")

if avg > 90 :
    print("Grade : A")
elif avg > 80 and avg < 90:
    print(f"Grade : B")
elif avg >= 70 and avg < 79:
    print(f"Grade : C")
elif avg >= 60 and avg < 69:
    print(f"Grade : D")
elif avg>0 and avg <= 59:
    print(f"Grade : F")
else:
    print(f"fail")