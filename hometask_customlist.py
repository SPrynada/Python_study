class Customlist(object):

    def __init__(self, elements=0):
        self.mylist = [0] * elements

    def __getitem__(self, index):
        return self.mylist[index]

    def __setitem__(self, index, value):
        self.mylist[index] = value

    def __str__(self):
        return str(self.mylist)

    def __add__(self, other):
        a = self.mylist.copy()
        for i in other:
            a.append(i)
        return a

    def append_(self, value):
        self.mylist.append(value)

    def pop_(self, index):
        self.mylist.pop(index)

    def insert_(self, index, value):
        self.mylist.insert(index, value)

    def remove_all(self, value):
        i = 0
        a = len(self.mylist)
        while i < a:
            if self.mylist[i] == value:
                self.mylist.remove(value)
                a -= 1
            else:
                i += 1
        else:
            pass

    def clear_(self):
        self.mylist.clear()

b = Customlist(3)
b[0] = 33
b[2] = 44
c = Customlist(5)
c[0] = 2
c[1] = 1
print('список b =', b, 'список c =', c)
d = b + c
print('список d = ', d)
print('список b = ', b)
print('список c =', c)
c.append_(4)
print(c)
c.pop_(0)
print(c)
c.insert_(1, 5)
print(c)
c.remove_all(0)
print(c)
c.clear_()
print(c)
