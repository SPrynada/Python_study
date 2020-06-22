import time
import random

def repeater(repeats):

    def decorator(func):

        def wrapper(*args):
            a = time.time()
            for i in range(repeats):

                c = func(*args)

            b = time.time()
            c = b - a

            return print(f"Время выполнения функции {func.__name__} {repeats} раз: {c}")
        return wrapper
    return decorator


@repeater(10)
def funct():
    aa = random.randint(0, 100)
    return print("результат funct = ", aa)


funct()