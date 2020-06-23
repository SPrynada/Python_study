# стек
my_stack = []

for i in range (0, 10):
    my_stack.append(i)

print("My stack: ", my_stack)

for i in range(0, 10):
    my_stack.pop()
    print(f'My {i}th stack:', my_stack)

# очередь
from collections import deque
my_que = deque()

for i in range (0, 10):
    my_que.append(i)

print("My que: ", my_que)

for i in range(0, 10):
    my_que.popleft()
    print(f'My {i}th que:', my_que)
