import sqlite3


# from datetime import datetime

class DataStudents:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


class StudentsGrades:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


def initianization():
    name_check = str(input('Введите Имя: '))
    password_check = str(input('Введите пароль: '))

    if (name_check == 'Admin' or 'admin') and password_check == '9999':
        print('Проверка пройдена, у вас права администратора')
        return 1
    else:
        return 2


def all_data():
    with DataStudents('lesson8.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM student')
        print(cursor.fetchall())


def studentsgrades():
    with StudentsGrades('lesson8.db') as conn:
        cursor = conn.cursor()
        student_number_ = int(input('Введите Номер студента: '))
        cursor.execute('SELECT subject, grade FROM grades WHERE student_number = ?', [student_number_])
        print(cursor.fetchall())


def inputstudent():
    with DataStudents('lesson8.db') as conn:
        cursor = conn.cursor()
        first_name_ = str(input('Введите Имя: '))
        last_name_ = str(input('Введите Фамилию: '))
        faculty_ = str(input('Введите Факультет: '))
        groupp_ = int(input('Введите Номер группы: '))
        student_number_ = int(input('Введите Номер студента: '))
        cursor.execute("INSERT INTO  student ('first_name', 'last_name', 'faculty', 'groupp', 'student_number') "
                       "VALUES (?, ?, ?, ?, ?)", (first_name_, last_name_, faculty_, groupp_, student_number_))
        print(cursor.fetchall())
        conn.commit()

def studentsdelete():
    with DataStudents('lesson8.db') as conn:
        cursor = conn.cursor()
        student_number_ = int(input('Введите Номер студента: '))
        cursor.execute("DELETE FROM student WHERE (student_number=?)", [student_number_])
        print(cursor.fetchall())
        conn.commit()

def inputgrade():
    with StudentsGrades('lesson8.db') as conn:
        cursor = conn.cursor()
        student_number_ = int(input('Введите Номер студента: '))
        subject_ = str(input('Введите Название предмета: '))
        grade_ = int(input('Введите оценку: '))
        cursor.execute("INSERT INTO  grades ('student_number', 'subject', 'grade') "
                       "VALUES (?, ?, ?)", (student_number_, subject_, grade_))
        print(cursor.fetchall())
        conn.commit()

def findstudent(st_number):
    with DataStudents('lesson8.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, faculty, grade FROM student "
                       "LEFT JOIN grades ON student.student_number=grades.student_number "
                       "WHERE student.student_number = ?", [st_number])
        print(cursor.fetchall())

def findstudent_grades():
    with DataStudents('lesson8.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT student.student_number, first_name, last_name, faculty, avg(grades.grade) "
                       "FROM student LEFT JOIN grades ON student.student_number=grades.student_number "
                       "GROUP BY student.student_number")
                       # "WHERE avg(grades.grade) = ?", [av_grade])
        print(cursor.fetchall())

allowed_functions = initianization()
# print(allowed_functions)

if allowed_functions == 1:
    required_functions = 3
    while required_functions in [1, 2, 3, 4, 5, 6, 7]:
        required_functions = int(input('Вам разрешены следующие действия:\n'
                                        'Добавить студента: введите 1\n'
                                        'Добавить оценки студента: введите 2\n'
                                        'Распечатать всех студентов: введите 3\n'
                                        'Распечатать оценки студента: введите 4\n'
                                        'Удалить запись студента: введите 5\n'
                                        'Найти данные студента по номеру: введите 6\n'
                                        'Найти студента по среднему баллу: введите 7\n'
                                        'Выйти из программы: введите любой другой символ\n'))
        if required_functions == 1:
            inputstudent()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 2:
            stopvalue = 0
            while stopvalue != 1:
                inputgrade()
                more_data = str(input('Еще будете добавлять оценки Студента: Y/ N - '))
                if more_data not in ['Y','y']:
                    stopvalue = 1
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 3:
            all_data()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 4:
            studentsgrades()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 5:
            studentsdelete()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 6:
            search_grade = float(input('Введите номер студента: '))
            findstudent(search_grade)
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 7:
            # search_grade = float(input('Введите средний бал для поиска: '))
            findstudent_grades()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0

if allowed_functions == 2:
    required_functions = 3
    while required_functions in [1, 2, 3, 4]:
        required_functions = int(input('Вам разрешены следующие действия:\n'
                                       'Распечатать всех студентов: введите 1\n'
                                       'Распечатать оценки студента: введите 2\n'
                                       'Найти данные студента по номеру: введите 3\n'
                                       'Найти студента по среднему баллу: введите 4\n'
                                       'Выйти из программы: введите любой другой символ\n'))
        if required_functions == 1:
            all_data()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 2:
            studentsgrades()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 3:
            search_grade = float(input('Введите номер студента: '))
            findstudent(search_grade)
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0
        elif required_functions == 4:
            # search_grade = float(input('Введите средний бал для поиска: '))
            findstudent_grades()
            if str(input('Вернуться в основное меню?: Y/ N - ')) not in ['Y','y']:
                required_functions = 0