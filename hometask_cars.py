class Cars:

    def __init__(self, type, number):
        self.type = type
        self.doors = number

    def driving(self, items):
        self.items = items
        print(self.type, "You can drive: ", items)


class Auto(Cars):

    def beep(self):
        print(self.type, ": hard beep")

class Track(Cars):

    def move(self):
        print("heavy drive: ", self.type)

    def driving(self, items):
        self.items = items
        print(self.type, "You can't drive: ", items)

a = Auto("Mazda", "AA9988BI")
b = Track("Volvo", "AA0333BO")

a.driving(3)
a.beep()
b.move()
b.driving(2)
