#Allow user to enter students, enter grades, view student list, view individual students
#Create dictionary in the format {'name': <student_name>, 'grades': []}
#Return dictionary
student_list = []

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        average = sum(self.grades) / len(self.grades)
        return average

def create_student():
    name = input("Please enter student's name: ")
    student_info = Student(name)
    return student_info

def add_grade(student, grade):
    #Append grade to student dictionary
    student.grades.append(grade)

def student_info(student):
    #Print name, grades and average of student
    print("{}, grades: {} , average grade: {}".format(student.name,
                            student.grades, student.average_grade()))

def show_students(students):
    #Print details for list of students
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        student_info(student)

def menu():
    # Allow user to add a student to student student_list
    # Allow user to add a grade to a student
    # Allow user to print a list of students
    # Exit application
    print("Welcome! Would you like to: ")
    print("a: Add a student?")
    print("b: Add a grade for a student?")
    print("c: See full student list?")
    print("d: See individual student info?")
    print("q: Quit")
    user_choice = input("Please type the letter corresponding to your choice: ")
    while user_choice != 'q':
        if user_choice == 'a':
            student_list.append(create_student())
        elif user_choice == 'b':
            student_id = int(input("Enter student ID#: "))
            student = student_list[student_id]
            new_grade = int(input("Enter grade you would like to add: "))
            add_grade(student, new_grade) #input student name and run add_grade
            print(student_list[student_id])
        elif user_choice == 'c':
            show_students(student_list)
        elif user_choice == 'd':
            input("Please enter student's ID#: ")
            print(student_info(student_list[student_id]))

        print("Welcome! Would you like to: ")
        print("a: Add a student?")
        print("b: Add a grade for a student?")
        print("c: See full student list?")
        print("d: See individual student info?")
        print("q: Quit")
        user_choice = input("Please type the letter corresponding to your choice: ")


menu()
