from domains import models as md
import input as ip
import math 
import os
 
dialogue_str = """
Menu:
0. Clear Screen
1. Add Student
2. Add Course
3. Input marks for a course
4. Show all students
5. Show all courses
6. Print marks for all Students of a Course
7. Sort students by GPA and show it
1337. Exit
Select an option: 
"""

def output():
    list_student = md.Student_list()
    list_course = md.Course_list()
    while True:
        choice = int(input(dialogue_str))
        if choice not in [0,1,2,3,4,5,6,7,1337]:
            print("Invalid choice. Try again.")
            continue
        if choice == 0:
            os.system('cls' if os.name == 'nt' else 'clear') # Window: cls != Linux: clear
        elif choice == 1:
            student = ip.input_student_dialogue()
            list_student.add_student(student)
        elif choice == 2:
            course = ip.input_course_dialogue()
            list_course.add_course(course)
        elif choice == 3:
            ip.input_mark(list_student, list_course)
        elif choice == 4:
            list_student.print_all_student()
        elif choice == 5:
            list_course.print_all_courses()
        elif choice == 6:
            list_course.print_all_courses()
            c_id = input("Enter course ID to view marks: ")
            print(f"Marks for course {c_id}:")
            for st in list_student.students:
                marks = st.mark.get(c_id, 'No marks entered')
                if(marks != 'No marks entered'):
                    marks = math.floor(marks)
                print(f"{st.name}: {marks}")
        elif choice == 7:
            list_student.calculate_GPA(list_course)
            list_student.sort_by_GPA_desc()
            print("Students sorted by GPA:")
            list_student.print_all_student()
        elif choice == 1337:
            print("Goodbye!!!")
            break
 
