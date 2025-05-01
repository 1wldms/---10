class Complex:
    def __init__(self, real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, operand):
        new_real = self.real + operand.real
        new_imaginary = self.imaginary + operand.imaginary
        return Complex(new_real, new_imaginary)
    
    def __sub__(self, operand):
        new_real = self.real - operand.real
        new_imaginary = self.imaginary - operand.imaginary
        return Complex(new_real, new_imaginary)
    
    def __mul__(self, operand):
        new_real = self.real  operand.real - self.imaginary  operand.imaginary
        new_imaginary = self.real  operand.imaginary + self.imaginary  operand.real
        return Complex(new_real, new_imaginary)
    
    def __neg__(self):
        new_real = -(self.real)
        new_imaginary = -(self.imaginary)
        
        return Complex(new_real, new_imaginary)
    
    def __str__(self):
        return f'{self.real} + {self.imaginary}i'


A = Complex(1,2)
B = Complex(3,4)
print(-A)
print(-B)
print(A + B)
print(A - B)
print(A * B)