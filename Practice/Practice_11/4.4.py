class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, course, grade):
        self.grades.setdefault(course, []).append(grade)


class Mentor:
    def __init__(self, name, surname,students):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.students = students

    def rate_hw(self, student, course, grade):
        if course in self.courses_attached and isinstance(student, Student):
            student.rate_hw(course, grade)


def calculate_average_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    if total_students == 0:
        return 0
    return total_grades / total_students


def calculate_average_lecture_grade(self,mentors, course,students):
    total_grades = 0
    total_mentors = 0
    for mentor in mentors:
        if course in mentor.courses_attached:
            total_grades += sum(grade for student in students if course in student.grades for grade in student.grades[course])
            total_mentors += len([student for student in students if course in student.grades])
    if total_mentors == 0:
        return 0
    return total_grades / total_mentors

student1 = Student("Евгений", "Жириновский", "мужской")
student2 = Student("Тарас", "Бульба", "мужской")

mentor1 = Mentor("Михаил", "Петрович",[student1,student2])
mentor2 = Mentor("Джон", "Уик",[student1,student2])

student1.add_course("Математика")
student1.add_course("Физика")
student2.add_course("Физика")

mentor1.courses_attached = ["Математика"]
mentor2.courses_attached = ["Физика"]

mentor1.rate_hw(student1, "Математика", 90)
mentor2.rate_hw(student1, "Физика", 85)
mentor2.rate_hw(student2, "Физика", 92)

average_grade_math = calculate_average_grade([student1, student2], "Математика")
average_grade_physics = calculate_average_grade([student1, student2], "Физика")
average_lecture_grade_math = calculate_average_lecture_grade([mentor1, mentor2], "Математика")
average_lecture_grade_physics = calculate_average_lecture_grade([mentor1, mentor2], "Физика")

print(f"Средняя оценка за Математику: {average_grade_math}")
print(f"Средняя оценка за Физику: {average_grade_physics}")
print(f"Средняя оценка за лекции по Математике: {average_lecture_grade_math}")
print(f"Средняя оценка за лекции по Физике: {average_lecture_grade_physics}")
