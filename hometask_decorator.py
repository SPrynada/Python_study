import datetime
import random

def repeater(repeats):

    def decorator(func):

        def wrapper(*args):

            for i in range(repeats):
                a = datetime.datetime.today()
                c = func(*args)

                b = datetime.datetime.today()
                c = b - a
                print(f"Время выполнения функции: {c}")
            return c
        return wrapper
    return decorator


@repeater(10)
def funct():
    aa = random.randint(0, 100)
    return print("результат funct = ", aa)


funct()