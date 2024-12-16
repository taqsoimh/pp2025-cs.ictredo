import numpy as np

class Student:
    def __init__(self, id: str, name: str, dob: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}
        self.gpa = 0
    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - DoB: {self.dob}"
    
    def cal_GPA(self, c_list) -> float:
        credits = []
        marks = []
        for c_id, mark in self.mark.items():
            for c in c_list.courses:
                if c.id == c_id:
                    credits.append(c.credit)
                    marks.append(mark)
        total_credit = sum(credits)
        marks = np.array(marks)
        weighted_sum = np.sum(marks * credits)
        self.gpa = weighted_sum / total_credit if total_credit != 0 else 0
        return self.gpa
class Course:
    def __init__(self, id: str, name: str, credit: int):
        self.id = id
        self.name = name
        self.credit = credit
    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - Credit: {self.credit}"

class Student_list:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def calculate_GPA(self, c_list):
        for st in self.students:
            st.cal_GPA(c_list)
    def sort_by_GPA_desc(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)
    def get_avg_GPA(self):
        if not self.students:
            return 0
        total_GPA = np.sum([st.gpa for st in self.students])
        return total_GPA / len(self.students)
    def print_all_student(self):
        for st in self.students:
            print(st)

class Course_list:
    def __init__(self):
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
    def print_all_courses(self):
        for c in self.courses:
            print(c)
