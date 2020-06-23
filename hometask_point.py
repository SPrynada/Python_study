class Point:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def __add__(self, other):
        new_a = self.a + other.get_a()
        new_b = self.b + other.get_b()
        new_c = self.c + other.get_c()
        return Point(new_a, new_b, new_c)

    def __sub__(self, other):
        new_a = self.a - other.get_a()
        new_b = self.b - other.get_b()
        new_c = self.c - other.get_c()
        return Point(new_a, new_b, new_c)

    def __mul__(self, other):
        new_a = self.a * other.get_a()
        new_b = self.b * other.get_b()
        new_c = self.c * other.get_c()
        return Point(new_a, new_b, new_c)

    def __truediv__(self, other):
        new_a = self.a / other.get_a()
        new_b = self.b / other.get_b()
        new_c = self.c / other.get_c()
        return Point(new_a, new_b, new_c)

    def __str__(self):
        return f'the new point has coordinates: [{self.a}, {self.b}, {self.c}]'


obj = Point(1, 2, 3)
obj2 = Point(1, 2, 3)

print("Adding: ", obj + obj2)
print("Substruction: ", obj - obj2)
print("Multiplication: ", obj * obj2)
print("Division: ", obj / obj2)