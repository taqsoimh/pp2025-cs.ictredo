import os

list_student = [] #list
list_course = [] #list

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

def print_marks_for_course():
    if not list_course:
        print("No courses have been added yet.")
        return
    c_id = input("Enter the Course ID: ")
    for c in list_course:
        if c["c_id"] == c_id:
            if "students" not in c:
                print(f"No marks recorded for the course: {c['c_name']} (ID: {c_id}).")
                return
            print(f"Marks for course: {c['c_name']} (ID: {c_id})")
            print("-" * 30)
            if "students" in c:
                for st in c["students"]:
                    print(f"    {st}: {c['students'][st]}")
            print("-" * 30)
            return
    print(f"Course with ID {c_id} not found.")

def print_all_students():
    if not list_student:
        print("No students have been added yet.")
        return
    print("-" * 30)
    print("All students:")
    for st in list_student:
        print(f"Name: {st["st_name"]} - ID: {st["st_id"]}")
    print("-" * 30)

def print_all_courses():
    if not list_course:
        print("No courses have been added yet.")
        return
    print("-" * 30)
    print("All courses:")
    for c in list_course:
        print(f"Name: {c["c_name"]} - ID: {c["c_id"]}")
    print("-" * 30)

def add_mark():
    # course => list of student => mark
    # course = {"students": {"s_id": mark}}
    c_id = input("Course ID: ")
    st_id = input("Student ID: ")
    mark = input("Mark: ")
    for c in list_course:
        if c["c_id"] == c_id:
            if "students" not in c:
                c["students"] = {}
            for st in list_student:
                if st["st_id"] == st_id:
                    c["students"][st_id] = mark
                    return
            print("Can't find this STUDENT !")
            return
    print("Can't find this COURSE !")
    
def main():
    while True:
        choice = int(input(dialogue_str))
        if choice not in [0,1,2,3,4,5,6,7]:
            print("Invalid choice. Try again.")
            continue
        if choice == 0:
            os.system('cls' if os.name == 'nt' else 'clear') # Window: cls != Linux: clear
        elif choice == 1:
            st = {}
            st["st_name"] = input("Student name: ")
            st["st_id"] = input("Student ID: ")
            list_student.append(st)
        elif choice == 2:
            c = {}
            c["c_name"] = input("Course name: ")
            c["c_id"] = input("Course ID: ")
            list_course.append(c)
        elif choice == 3:
            add_mark()
        elif choice == 4:
            print_all_students()
        elif choice == 5:
            print_all_courses()
        elif choice == 6:
            print_marks_for_course()
        elif choice == 7:
            print("Bai bai <3 <3 hihiihhihihiihhihihhhiihihihi")
            break

if __name__ == "__main__":
    main()
