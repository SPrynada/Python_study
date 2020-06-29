from datetime import datetime



class User:

    list_users = []

    def __init__(self, name_, password='00000000', role='User', article = None):
        self.list_users.append(self)
        self.name_ = name_
        self.password = password
        self.registration_date = datetime.now()
        self.role = role
        self.article = article

    def __str__(self):
        return f'Пользователь {self.name_}, зарегистрирован: {self.registration_date}, статус {self.role}'

    def authorization(self, name_check):
        password_check = str(input('Введите пароль: '))
        if name_check == self.name_ and password_check == self.password:
            print('проверка пройдена')
            return True
        else:
            return print('Пароль неверный')

    def get_article(self):
        return self.article, self.publishing_date

    def set_article(self, value):
        self.publishing_date = datetime.now()
        self.article = value


user_base = User('Vasil', '9999bb', 'Admin')
user1 = User('Timon', '222sss')
user2 = User('Petya', '888ddd')
user3 = User('Roma', '1111aa')
user4 = User('Dima', '555eee')

def check_password(x):
    if len(x) < 6:
        print('Длина пароля менее 6ти символов')
        return False
    elif ((any(map(str.isdigit,x)) and any(map(str.isalpha, x)))) == False:
        print('Пароль не соответствует минимальным требованиям')
        return False
    else:
        return True


def initialization():

    n = False
    while n != True:
        a = str(input('Введите имя пользователя: '))
        for user in User.list_users:
            if user.name_ == a:
                print('Пользователь с таким именем существует.')
                break
        else:
            n = True

    b = 'Y'
    while b == 'Y':
        c = str(input('Введите пароль (длина не менее 6 символов, буквы и цифры): '))
        if check_password(c) == True:
            c2 = str(input('Повторите пароль: '))
            while c != c2:
                c2 = str(input('Повтор неверный. Повторите ввод пароля: '))
            else:
                user_n = User(a, c)
                b = 'N'
                break
result1 = False
def admin_function():

    if str(input('Вы хотите распечатать перечень пользователей (Y/N)? ')) == 'Y':
        print('Перечень всех пользователей:')
        for user in User.list_users:
            print(user)
    if str(input('Вы хотите распечатать все публикации (Y/N)? ')) == 'Y':
        print('Печать всех статей:')
        for user in User.list_users:
            if user.article != None:
                print(f'Статья пользователя {user.name_}: {user.article}, дата публикации: {user.publishing_date}')
    else:
        result1 = True


def user_access():
    a = str(input('Введите имя пользователя: '))
    n = False
    while n != True:
        for user in User.list_users:
            if user.name_ == a and user.role != 'Admin':
                authorization_attempt = 1
                while authorization_attempt <= 5:
                    if user.authorization(a) == True:
                        user.set_article(input('Введите статью: '))
                        print('Статья заведена')
                        result = True
                        break
                    else:
                        authorization_attempt += 1
                else:
                    print('Количество попыток превысило граничное значение')
                    break
            elif user.name_ == a and user.role == 'Admin':
                authorization_attempt = 1
                while authorization_attempt <= 3:
                    if user.authorization(a) == True:
                        admin_function()
                        result = True
                        break
                    else:
                        authorization_attempt += 1
                else:
                    print('Количество попыток превысило граничное значение')
                    result = True
                    break
                break
            break
        else:
            if str(input('Пользователя с таким именем не существует. Желаете зарегистрироваться (Y/N)? ')) == 'Y':
                initialization()
                if str(input('Желаете опубликовать статью (Y/N)? ')) == 'Y':
                    user.set_article(input('Введите статью: '))
                    print('Статья заведена')
                result = True
            break
    return result

result1 = user_access()
if result1 == True:
    d = str(input('Желаете зайти под другим именем? Введите Y или N: '))
    if d == 'Y':
        user_access()

