
class Student:
    def init(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def str(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания:  {self.get_average_grade_of_student()}\n"
                f"Курсы в процессе обучения: {self.courses_in_progress} \n"
                f"Завершённые курсы: {self.finished_courses}")

    def get_average_grade_of_student(self):
        grades_dictionary = self.grades
        n = len(grades_dictionary)
        sum_grades = sum([sum(grades_dictionary[x]) for x in grades_dictionary])
        return sum_grades / n

    def bool(self):
        if self.get_average_grade_of_student() == 10.0:
            return True
        else:
            return False

    def int(self):
        return len(self.finished_courses) + len(self.courses_in_progress)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached and 10 >= grade > 0:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Введите число от 1 до 10 для отметки')


class Mentor:
    def init(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        # self.students = students
        self.grades = {}

    '''def rate_hw(self, student, course, grade):
        if course in self.courses_attached and isinstance(student, Student):
            student.rate_hw(course, grade)'''

    def rate_hw(self, student, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course][student] = grade
            else:
                self.grades[course] = {student: grade}

    def int(self):
        return len(self.courses_attached)


'''def calculate_average_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    if total_students == 0:
        return 0
    return total_grades / total_students


def calculate_average_lecture_grade(mentors, course, students):
    total_grades = 0
    total_mentors = 0
    for mentor in mentors:
        if course in mentor.courses_attached:
            total_grades += sum(
                grade for student in students if course in student.grades for grade in student.grades[course])
            total_mentors += len([student for student in students if course in student.grades])
    if total_mentors == 0:
        return 0
    return total_grades / total_mentors'''


class Reviewer(Mentor):
    def init(self, name, surname):
        super().init(name, surname)
        self.reviewer_courses = []

    def add_reviewer_course(self, course_name):
        self.reviewer_courses.append(course_name)

    def str(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname}")

    def rate_student(self, student, course, grade):
        if (
                course in student.courses_in_progress or course in student.finished_courses) and course in self.courses_attached and (
                10 >= grade > 0):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print('Выставлена неправильная отметка, число должно быть от 1 до 10')

    def bool(self):
        pass

class Lecturer(Mentor):
    def init(self, name, surname):
        super().init(name, surname)
        self.lecturer_courses = []

    '''def add_lecturer_course(self, course_name):
        self.lecturer_courses.append(course_name)'''

    def str(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {self.get_average_grade_of_lector()}")

    def get_average_grade_of_lector(self):
        grades_dictionary = self.grades
        n = len(grades_dictionary)
        sum_grades = sum([sum(grades_dictionary[x]) for x in grades_dictionary])
        return sum_grades / n

    def bool(self):
        if self.get_average_grade_of_lector() == 10.0:
            return True
        else:
            return False


# 4.3
student1 = Student("Денис", "Степанов", "Мужской")
reviewer1 = Reviewer("Андрей", "Пучков")
reviewer2 = Reviewer('Артём', 'Беспечалов')
lecturer1 = Lecturer("Матвей", "Афанасьев")
print()
student1.add_courses('Физика')
student1.courses_in_progress.append("Математика")

reviewer1.courses_attached.append("Математика")
reviewer2.courses_attached.append('Физика')
reviewer1.courses_attached.append("Математика")
lecturer1.courses_attached.append("Математика")

reviewer2.rate_student(student1, 'Физика', 10)
reviewer1.rate_student(student1, "Математика", 5)
student1.rate_lecturer(lecturer1, "Математика", 10)

print(str(student1))
print(f"Курсов окончено + Курсы в процессе обучения: {int(student1)}")
print(f"Является ли студент отличником: {bool(student1)}")
print()
print(str(lecturer1))
print(f"Прикреплено предметов: {int(lecturer1)}")
print(f"Лектор красавчик?: {bool(lecturer1)}")
print()
print(str(reviewer1))
print(f"Прикреплено предметов: {int(reviewer1)}")