'''
This program supports python3
Command to execute : python3 filename.py
Input : 2 3
        5 6
'''
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    def __mul__(self, no):
        return Complex(self.real*no.real + self.imaginary*no.imaginary*(-1), self.imaginary*no.real + self.real*no.imaginary)
    
    def __truediv__(self, no):
        sr, si, oor, oi = self.real, self.imaginary, no.real, no.imaginary
        r = float(oor**2 + oi**2)
        return Complex((sr*oor+si*oi)/r, (si*oor-sr*oi)/r)
    
    def mod(self):
        return '%s+0.00i'%"{0:.2f}".format(math.sqrt(self.real**2 + self.imaginary**2))

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
