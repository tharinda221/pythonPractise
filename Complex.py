
import math
__author__ = 'Ehelepola'

class Complex(object):
    def __init__(self,real,imaginary):

        self.real=real
        self.imaginary=imaginary

    def __add__(self, other):

        real=self.real+other.real
        imaginary=self.imaginary+other.imaginary

        return Complex(real,imaginary)

    def __sub__(self, other):

        real=self.real-other.real
        imaginary=self.imaginary-other.imaginary

        return Complex(real,imaginary)

    def __mul__(self, other):

        real=self.real*other.real - self.imaginary*other.imaginary
        imaginary=self.real*other.imaginary + other.real*self.imaginary

        return Complex(real,imaginary)
    def div(self, other):

        x = float(other.real ** 2 + other.imaginary ** 2)
        y = self * Complex(other.real, -other.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)
    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)
    def __str__(self):

        if self.imaginary == 0:
            result = "%.2f" % (self.real)
        elif self.real == 0:
            result = "%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f + %.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f - %.2fi" % (self.real, abs(self.imaginary))
        return result


C = map(float, input().split())
D = map(float, input().split())

x = Complex(*C)
y = Complex(*D)
final = [x+y, x-y, x*y, x.div(y), x.mod(), y.mod()]
print('\n'.join(map(str, final)))


