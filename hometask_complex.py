class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep

    def __add__(self, other):
        if isinstance(other, Complex):
            newRe = self.re + other.re
            newIm = self.im + other.im
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re + other
            newIm = self.im
        return Complex(newRe, newIm)

    def __sub__(self, other):
        if isinstance(other, Complex):
            newRe = self.re - other.re
            newIm = self.im - other.im
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re - other
            newIm = self.im
        return Complex(newRe, newIm)

    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        return Complex(newRe, newIm)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            newRe = (self.re * other.re + self.im * other.im) / (other.re **2 + other.im**2)
            newIm = (self.im * other.re - self.re * other.im) / (other.re **2 + other.im**2)
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re / other
            newIm = self.im / other
        return Complex(newRe, newIm)


a = Complex(-2, 1)
print("Первое значение: ", a)
b = Complex(1, -1)
print("Второе значение: ", b)
c = 2
print(f"Сумма {a} и {b}:", a + b)
print(f"Сумма {a} и {c}:", a + c)
print(f"Разность {a} и {b}:", a - b)
print(f"Разность {a} и {c}:", a - c)
print(f"Произведение {a} и {b}:", a * b)
print(f"Произведение {a} и {c}:", a * c)
print(f"Деление {a} и {b}:", a / b)
print(f"Деление {a} и {c}:", a / c)