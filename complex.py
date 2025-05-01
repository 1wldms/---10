class Complex:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __add__(self, operand):
        new_a = self.a + operand.a
        new_b = self.b + operand.b
        return Complex(new_a, new_b)
    
    def __str__(self):
        return f'{self.a} + {self.b}i'
    
    def dd

A = Complex(1,2)
B = Complex(3,4)
C = A + B
print(C)