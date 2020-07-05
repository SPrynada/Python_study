from datetime import datetime
import time
from threading import Thread, enumerate

def do_time():
    def outer(fn):
        def wrapper(name_, t):
            start = datetime.now()
            result = fn(name_, t)
            print(f'Time of the thread {name_} is: ', datetime.now()-start)

            return result
        return wrapper

    return outer

@do_time()
def do_threads(name_, t):
    print(f'Operation {name_} started')
    time.sleep(t)
    print(f'Operation {name_} ended in {t} seconds')

start = datetime.now()

t = Thread(target=do_threads, args=('Sleeping', 1), daemon=True)
t2 = Thread(target=do_threads, args=('Blocking', 6), daemon=True)
t3 = Thread(target=do_threads, args=('IO bound', 3), daemon=True)
t4 = Thread(target=do_threads, args=('No name', 3), daemon=True)

t.start(), t2.start(), t3.start(), t4.start()
t.join(), t2.join(), t3.join(), t4.join()

print(t.is_alive(), t2.is_alive(), t3.is_alive(), t4.is_alive())

print(f'Total time {datetime.now() - start}')