class ComplexNumber:

    def __init__(self, re, im):
        self.real = re
        self.imaginary = im

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real) - (self.imaginary * other.imaginary),
                              (self.imaginary * other.real) + (self.real * other.imaginary))

    def __truediv__(self, other):
        if other.real**2 + other.imaginary**2:

            return ComplexNumber(((self.real * other.real) + (self.imaginary * other.imaginary)) / (other.real**2 + other.imaginary**2),
                              ((self.imaginary * other.real)-(self.real * other.imaginary)) /(other.real**2 + other.imaginary**2) )

        else:
            return " Modulus must be different from zero! "

    def __str__(self):

        znak = " - " if self.imaginary < 0 else " + "
        return str(self.real) + znak + str(abs(self.imaginary)) + "i"


z1 = ComplexNumber(2,1)
z2 = ComplexNumber(-1,3)
z3 = ComplexNumber(1,0)


z = z1/z3
print(z)