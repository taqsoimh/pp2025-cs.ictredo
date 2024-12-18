from domains import models as md

def input_student_dialogue():
    st_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    student = md.Student(st_id, name, dob)
    check_unique = True
    try:
        with open("students.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" - ")
                existing_id = parts[0].split(": ")[1] # Giả định st_id là phần tử đầu tiên
                if existing_id == st_id:
                    check_unique = False

    except FileNotFoundError:
        check_unique = True  # Nếu file chưa tồn tại, coi như st_id là duy nhất

    if check_unique:
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(f"{student}\n")
            return student
    else:
        print("Student ID is existed. Please try again.")
    

def input_course_dialogue():
    c_id = input("Enter course ID: ")
    c_name = input("Enter course name: ")
    credit = input("Enter course credit: ")
    course = md.Course(c_id, c_name, credit)
    check_unique = True
    try:
        with open("courses.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" - ")
                existing_id = parts[0].split(": ")[1]  # Giả định c_id là phần tử đầu tiên
                if existing_id == c_id:
                    check_unique = False
    except FileNotFoundError:
        check_unique = True  # Nếu file chưa tồn tại, coi như c_id là duy nhất

    if check_unique:
        with open("courses.txt", "a", encoding="utf-8") as file:
            file.write(f"{course}\n")
            return course
    else:
        print("Course ID is existed. Please try again.")

def input_mark(list_student, list_course):
    list_course.print_all_courses()
    c_id = input("Enter course ID to view marks: ")
    print(f"Marks for course {c_id}:")
    for c in list_course.courses:
        if(c.id == c_id):
            list_student.print_all_student()
            st_id = input("Input Student ID that you want to add mark: ")
            for st in list_student.students:
                if(st.id == st_id):
                    inp_mark = float(input("Input mark: "))
                    st.mark[c_id] = float(inp_mark)
                    f = open("marks.txt", "a")
                    f.write(f"{st_id} {c_id} {inp_mark}\n")
                    f.close()