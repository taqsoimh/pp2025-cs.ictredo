import os
class Student:
    def __init__(self, id: str, name: str, dob: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}
    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - DoB: {self.dob}"
class Course:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
    def __str__(self):
        return f"ID: {self.id} - Name: {self.name}"


class Student_list:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def print_all_student(self):
        for st in self.students:
            print(st)
class Course_list:
    def __init__(self):
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
    def print_all_course(self):
        for c in self.courses:
            print(c)

dialogue_str = """
Menu:
0. Clear Screen
1. Add Student
2. Add Course
3. Input marks for a course
4. Show all students
5. Show all courses
6. Print marks for all Students of a Course
7. Exit
Select an option: 
"""

def main():
    list_student = Student_list()
    list_course = Course_list()
    while True:
        choice = int(input(dialogue_str))
        if choice not in [0,1,2,3,4,5,6,7]:
            print("Invalid choice. Try again.")
            continue
        if choice == 0:
            os.system('cls' if os.name == 'nt' else 'clear') # Window: cls != Linux: clear
        elif choice == 1:
            st_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            student = Student(st_id, name, dob)
            list_student.add_student(student)
        elif choice == 2:
            c_id = input("Enter course ID: ")
            c_name = input("Enter course name: ")
            course = Course(c_id, c_name)
            list_course.add_course(course)
        elif choice == 3:
            c_id = input("Enter course ID to view marks: ")
            print(f"Marks for course {c_id}:")
            for c in list_course.courses:
                if(c.id == c_id):
                    list_student.print_all_student()
                    st_id = input("Input Student ID that you want to add mark: ")
                    for st in list_student.students:
                        if(st.id == st_id):
                            inp_mark = input("Input mark: ")
                            st.mark[c_id] = float(inp_mark)
        elif choice == 4:
            list_student.print_all_student()
        elif choice == 5:
            list_course.print_all_course()
        elif choice == 6:
            list_course.print_all_course();
            c_id = input("Enter course ID to view marks: ")
            print(f"Marks for course {c_id}:")
            for st in list_student.students:
                marks = st.mark.get(c_id, 'No marks entered')
                print(f"{st.name}: {marks}")
        elif choice == 1337:
            print("GoodBye!!!")
            break

if __name__ == "__main__":
    main()
