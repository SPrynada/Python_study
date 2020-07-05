from datetime import datetime
import requests
import os
from threading import Thread

def do_thread():

    def outer(fn):
        def wrapper(getjpg, namejpg):
            start = datetime.now()
            print('Operation started')
            result = fn(getjpg, namejpg)
            print(f'download from {getjpg} is ended, time: ', datetime.now()-start)

            return result
        return wrapper
    return outer

dirname = 'pictures'
if os.path.exists(dirname) == False:
    os.mkdir(dirname)

@do_thread()
def get_jpg(getjpg, namejpg):

    response = requests.get(getjpg)
    data = response.content
    with open(dirname+'/'+namejpg, 'wb') as f:
        f.write(data)

start = datetime.now()

picture1 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/4073/4887709225_031137dd8f_b_d.jpg', 'arctic-tern.jpg'),
           daemon=True)
picture2 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/2305/3534487277_6dd9a4fdc3_b_d.jpg', 'thrush.jpg'),
           daemon=True)
picture3 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/4045/4398048058_fd251fe712_b_d.jpg', 'gibbon.jpg'),
           daemon=True)
picture4 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/8343/8193388094_7245b08111_b_d.jpg', 'grey-owl.jpg'),
           daemon=True)
picture5 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/8326/8423545071_a4529f3b90_b_d.jpg', 'husky.jpg'),
           daemon=True)
picture6 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/7245/7188586822_511290f823_b_d.jpg', 'tiger.jpg'),
           daemon=True)
picture7 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/3632/3323037563_ecdced6abd_b_d.jpg', 'puma.jpg'),
           daemon=True)
picture8 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/1235/4733823624_a758c8e8e9_b_d.jpg', 'wolf.jpg'),
           daemon=True)
picture9 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/2465/3643453033_98050db92c_b_d.jpg', 'leopard.jpg'),
           daemon=True)
picture10 = Thread(target=get_jpg,
           args=('https://live.staticflickr.com/125/324174667_0c1640e178_b_d.jpg', 'night-heron.jpg'),
           daemon=True)
picture1.start(), picture2.start(), picture3.start(), picture4.start(), picture5.start()
picture6.start(), picture7.start(), picture8.start(), picture9.start(), picture10.start()
picture1.join(), picture2.join(), picture3.join(), picture4.join(), picture5.join()
picture6.join(), picture7.join(), picture8.join(), picture9.join(), picture10.join()
