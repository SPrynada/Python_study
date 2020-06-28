from datetime import datetime

class Person:

    def __init__(self, name_, birth_date):
        self.name_ = name_
        self.birth_date = birth_date

    def age(self):
        age = (datetime.now() - datetime.strptime(self.birth_date, '%Y/%m/%d')) // 365
        print(age.days)
        return age.days

    def search_age(self, value2):
        if self.age() == value2:
            print(self)

class Abiturient(Person):

    list_abiturients = []

    def __init__(self, name_, birth_date, faculty):
        super().__init__(name_, birth_date)
        self.faculty = faculty

    def __str__(self):
        return f'Абитуриент {self.name_}, дата рождения: {self.birth_date}, факультет {self.faculty}'

    def age(self):
        age = (datetime.now() - datetime.strptime(self.birth_date, '%Y/%m/%d')) // 365
        return age.days

    def search_age(self, value2):
        if self.age() == value2:
            print(Abiturient.name_)

abiturient1 = Abiturient('Ivanov', '2002/10/01', 'Mathematics')
Abiturient.list_abiturients.append(abiturient1)
abiturient2 = Abiturient('Sidorov', '2001/01/20', 'Chemistry')
Abiturient.list_abiturients.append(abiturient2)

print('Список абитурентов:')
for abiturient in Abiturient.list_abiturients:
    print(abiturient)

for abiturient in Abiturient.list_abiturients:
    print(f'Возраст абитуриента {abiturient.name_} '
          f'составляет {abiturient.age()} лет')


class Student(Abiturient):

    list_students = []

    def __init__(self, name_, birth_date, faculty, course):
        super().__init__(name_, birth_date, faculty)
        self.course = course

    def __str__(self):
        return f'Студент {self.name_}, дата рождения: {self.birth_date}, факультет {self.faculty}, курс {self.course}й'

    def age(self):
        age = (datetime.now() - datetime.strptime(self.birth_date, '%Y/%m/%d')) // 365
        return age.days


student1 = Student('Petrov', '2001/10/10', 'Mathematics', 2)
Student.list_students.append(student1)
student2 = Student('Vasechkin', '2000/05/15', 'Chemistry', 3)
Student.list_students.append(student2)

print('Список студентов:')
for student in Student.list_students:
    print(student)
for student in Student.list_students:
    print(f'Возраст студента {student.name_} '
          f'составляет {student.age()} лет')


class Teacher(Abiturient):

    list_teachers = []

    def __init__(self, name_, birth_date, faculty, position, start_teaching):
        super().__init__(name_, birth_date, faculty)
        self.position = position
        self.start_teaching = start_teaching

    def __str__(self):
        return (f'Преподаватель {self.name_}, дата рождения: {self.birth_date}, факультет {self.faculty},'
               f'должность {self.position}, преподает с {self.start_teaching}')


    def age(self):
        age = (datetime.now() - datetime.strptime(self.birth_date, '%Y/%m/%d')) // 365
        return age.days

    def months_teaching(self):
        months = (datetime.now() - datetime.strptime(self.start_teaching, '%Y/%m/%d')) // 30
        return months.days


teacher1 = Teacher('Zeneka', '1978/09/07', 'Mathematics', 'dean', '2018/10/1')
Teacher.list_teachers.append(teacher1)
teacher2 = Teacher('Oligarh', '1980/05/5', 'Chemistry', 'assistant', '2010/1/1')
Teacher.list_teachers.append(teacher2)

print('Список преподавателей:')
for teacher in Teacher.list_teachers:
    print(teacher)
for teacher in Teacher.list_teachers:
    print(f'Возраст преподавателя {teacher.name_} '
          f'составляет {teacher.age()} лет, '
          f'стаж составляет {teacher.months_teaching()} месяцев')


for abiturient in Abiturient.list_abiturients:
    if abiturient.age() >= 17:
        if abiturient.age() <= 21:
            print(f'Найден абитуриент возраста {abiturient.age()} (в диапазоне: 17 - 20 лет) - {abiturient.name_}')

for student in Student.list_students:
    if student.age() >= 18:
        if student.age() <= 21:
            print(f'Найден студент возраста {student.age()} (в диапазоне: 18 - 21 лет) - {student.name_}')

for teacher in Teacher.list_teachers:
    if teacher.age() >= 30:
        if teacher.age() <= 50:
            print(f'Найден студент возраста {teacher.age()} (в диапазоне: 30 - 50 лет) - {teacher.name_}')