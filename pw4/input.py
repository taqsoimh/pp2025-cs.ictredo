import domains as dm
def input_student_dialogue():
    st_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    student = dm.Student(st_id, name, dob)
    return student

def input_course_dialogue():
    c_id = input("Enter course ID: ")
    c_name = input("Enter course name: ")
    credit = input("Enter course credit: ")
    course = dm.Course(c_id, c_name, credit)
    return course

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
                    inp_mark = input("Input mark: ")
                    st.mark[c_id] = float(inp_mark)