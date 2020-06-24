# стек
class Stack:

    def __init__(self, my_stack):
        self.my_stack = my_stack
        self.my_stack = []

    def appending(self, symb):
        self.my_stack.append(symb)

    def excludng(self):
        self.my_stack.pop()

for i in range(0,10):
    a = Stack.appending(i)

print("My stack: ", a)

for i in range(0, 10):
    Stack.excludng()
    print(f'My {i}th stack:', a)
#
# # очередь
from collections import deque
class Que:

    def __init__ (self, my_que):
        self.my_que = my_que
        self.my_que = deque()

    def appending(self, symb):
        self.my_que.append(symb)

    def excludng(self):
        self.my_que.popleft()

for i in range(0, 10):
    a = Que.appending(i)

print("My que: ", a)

for i in range(0, 10):
    a.excluding()
    print(f'My {i}th que:', a)
