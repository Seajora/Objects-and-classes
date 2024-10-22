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

    def rate_lecturer(self, lecturer, course_name, grade):  # оценка студентами лекторов
        if isinstance(lecturer, Lecturer) and course_name in self.courses_in_progress and \
                course_name in lecturer.courses_attached and 1 <= grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # магический метод печати
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {round(self.avg_grade(), 2)}\n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.courses_in_progress))}\n" \
               f"Завершенные курсы: {', '.join(map(str, self.finished_courses))}"

    def avg_grade(self):  # средняя оценка
        overall_grade = 0  # счетчик суммы оценок
        grades_count = 0  # счетчик количества оценок
        if len(self.grades) == 0:  # если длина списка оценки == 0
            return 0  # то средняя оценка 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:  # пока не прокрутим все оценки
                    for grade in grades:
                        overall_grade += grade  # сумма оценок + текущая оценка из цикла
                        grades_count += 1  # кол-во оценок ++1
            return overall_grade / grades_count  # сумма оценок/количество оценок

    def __lt__(self, other):  # сравнение студентов по средней оценке за лекции
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()  # true or false
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # создаем дочерний класс Lecturer от родительского Mentor
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):  # магический метод печати
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(self.avg_grade(), 2)}"

    def avg_grade(self):  # метод оценки лектора
        overall_grade = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                overall_grade += grade
            return overall_grade / len(self.grades)
        else:
            return 0

    def __lt__(self, other):  # метод сравнения оценок лекторов
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return "Ошибка"


class Reviewer(Mentor):  # Создаем дочерний класс Reviewer от родительского Mentor
    def __int__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):  # перегрузка магический метод печати
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):  # Выставление оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ivan', 'Ivanov', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Ira', 'Petrova', 'female')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer("Alex", "Smirnov")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer = Reviewer("Elena", "Ivanova")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Git', 6)
cool_reviewer.rate_hw(best_student, 'Git', 5)

cool_reviewer.rate_hw(bad_student, 'Git', 7)
cool_reviewer.rate_hw(bad_student, 'Git', 6)
cool_reviewer.rate_hw(bad_student, 'Python', 4)
cool_reviewer.rate_hw(bad_student, 'Python', 5)

cool_lecturer = Lecturer('Denis', 'Denisov')
cool_lecturer.courses_attached += ['Python']

def_lecturer = Lecturer('Mark', 'Markov')
def_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, "Python", 9)
best_student.rate_lecturer(cool_lecturer, "Python", 9)

bad_student.rate_lecturer(def_lecturer, "Python", 7)
bad_student.rate_lecturer(def_lecturer, "Python", 6)

print(cool_lecturer)
print()
print(cool_reviewer)
print()
print(best_student)
print()
print(best_student > bad_student)
print(def_lecturer > cool_lecturer)
