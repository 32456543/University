class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_courses = []

    def add_lecturer_course(self, course_name):
        self.lecturer_courses.append(course_name)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviewer_courses = []

    def add_reviewer_course(self, course_name):
        self.reviewer_courses.append(course_name)



lecturer = Lecturer("Лариса", "Васильевна")
lecturer.add_lecturer_course("Химия")
print(lecturer.name, lecturer.surname, lecturer.lecturer_courses)

reviewer = Reviewer("Надежда", "Алесандровна")
reviewer.add_reviewer_course("Информатика")
print(reviewer.name, reviewer.surname, reviewer.reviewer_courses)

#student = Student("Евгений", "Коршиков", "мужской")
#student.add_courses("Прикладная информатика")
#print(student.name, student.surname, student.gender, student.finished_courses)
