from domains import models as md
import input as ip
import math 
import os
import zipfile

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

def compress_files():
    with zipfile.ZipFile('students.dat', 'w') as zipf:
        for filename in ['students.txt', 'courses.txt', 'marks.txt']:
            zipf.write(filename)

def decompress_files():
    with zipfile.ZipFile('students.dat', 'r') as zipf:
        zipf.extractall()

def output():
    decompress_files()
    list_student = md.Student_list()
    list_course = md.Course_list()
    fin_st = open("students.txt", "r")
    fin_course = open("courses.txt", "r")
    fin_mark = open("marks.txt", "r")
    for line in fin_st:
        parts = line.strip().split(" - ")
        student = md.Student(parts[0].split(": ")[1], parts[1].split(": ")[1], parts[2].split(": ")[1])
        list_student.add_student(student)
    for line in fin_course:
        parts = line.strip().split(" - ")
        course = md.Course(parts[0].split(": ")[1], parts[1].split(": ")[1], parts[2].split(": ")[1])
        list_course.add_course(course)
        
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
            for line in fin_mark:
                st_id = line.split()[0]
                c_id = line.split()[1]
                mark = line.split()[2]
                for st in list_student.students:
                    if(st.id == st_id):
                        st.mark[c_id] = float(mark)
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

    compress_files()
    fin_st.close()
    fin_course.close()
 