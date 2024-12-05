
students = []
courses = []
marks = {}

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
    students.append((student_id, name, dob))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((course_id, name))

def select_course_and_input_marks():
    if not courses:
        print("No courses available.")
        return

    print("Available courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course[1]} (ID: {course[0]})")
    
    course_index = int(input("Select a course by number: ")) - 1
    if course_index < 0 or course_index >= len(courses):
        print("Invalid selection.")
        return
    
    course_id = courses[course_index][0]
    marks[course_id] = {}
    for student in students:
        mark = float(input(f"Enter marks for student {student[1]} (ID: {student[0]}): "))
        marks[course_id][student[0]] = mark

# Listing functions
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks_for_course():
    if not courses:
        print("No courses available.")
        return

    print("Available courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course[1]} (ID: {course[0]})")
    
    course_index = int(input("Select a course by number: ")) - 1
    if course_index < 0 or course_index >= len(courses):
        print("Invalid selection.")
        return
    
    course_id = courses[course_index][0]
    if course_id not in marks:
        print(f"No marks entered for course {courses[course_index][1]} yet.")
        return
    
    print(f"Marks for course {courses[course_index][1]}:")
    for student in students:
        student_id = student[0]
        student_name = student[1]
        student_mark = marks[course_id].get(student_id, "N/A")
        print(f"Student: {student_name} (ID: {student_id}), Mark: {student_mark}")

num_students = input_number_of_students()
for _ in range(num_students):
    input_student_info()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_course_info()

while True:
    print("\nMenu:")
    print("1. List courses")
    print("2. List students")
    print("3. Input marks for a course")
    print("4. Show student marks for a given course")
    print("5. Exit")
    
    choice = int(input("Select an option: "))
    if choice == 1:
        list_courses()
    elif choice == 2:
        list_students()
    elif choice == 3:
        select_course_and_input_marks()
    elif choice == 4:
        show_student_marks_for_course()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
