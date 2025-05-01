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


A = Complex(1,2)
B = Complex(3,4)
print(-A)
print(-B)
print(A + B)
print(A - B)
print(A * B)