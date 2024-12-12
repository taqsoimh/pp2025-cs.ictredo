import os
class Student:
    def __init__(self, id: str, name: str, dob: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}
    
class Course:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

list_student = [] #list
list_course = [] #list

def add_mark():
    print_all_courses()
    c_id = input("Input Course ID:")
    for course in list_course:
        if(course.id == c_id):
            print_all_students()
            st_id = input("Input Student ID that you want to add mark: ")
            for st in list_student:
                if(st.id == st_id):
                    st.mark[c_id] = input("Input mark: ")
def input_student():
    st_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    student = Student(st_id, name, dob)
    list_student.append(student)

def input_course():
    c_id = input("Enter course ID: ")
    c_name = input("Enter course name: ")
    course = Course(c_id, c_name)
    list_course.append(course)

def print_all_courses():
    print("Courses:")
    for course in list_course:
        print(f"{course.id}: {course.name}")
    print("-"*5)

def print_all_students():
    print("Student:")
    for st in list_student:
        print(f"{st.id} - {st.name} - {st.dob}")
    print("-"*5)

def print_mark():
    print_all_courses();
    c_id = input("Enter course ID to view marks: ")
    print(f"Marks for course {c_id}:")
    for st in list_student:
        marks = st.mark.get(c_id, 'No marks entered')
        print(f"{st.name}: {marks}")


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
    while True:
        choice = int(input(dialogue_str))
        if choice not in [0,1,2,3,4,5,6,7]:
            print("Invalid choice. Try again.")
            continue
        if choice == 0:
            os.system('cls' if os.name == 'nt' else 'clear') # Window: cls != Linux: clear
        elif choice == 1:
            input_student()
        elif choice == 2:
            input_course()
        elif choice == 3:
            add_mark()
        elif choice == 4:
            print_all_students()
        elif choice == 5:
            print_all_courses()
        elif choice == 6:
            print_mark()
        elif choice == 7:
            print("Bai bai <3 <3 hihiihhihihiihhihihhhiihihihi")
            break

if __name__ == "__main__":
    main()