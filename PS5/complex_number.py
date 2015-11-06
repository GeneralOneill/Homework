class complex:
    def __initi__(self, real_num, complex_num):
        self.real = real_num
        self.complex = complex_num

    def set_real(self, real_num):
        self.real = real_num
    def set_complex(self, complex_num):
        self.complex = complex_num
    def get_real(self):
        return self.real
    def get_complex(self):
        return self.complex
    def copy(self):
        return complex(self.get_real, self.get_complex)

    def add(self, other):
        return complex(self.get_real + other.get_real, self.get_complex + other.get_complex)

    def subtract(self, other):
        return complex(self.get_real - other.get_real, self.get_complex - other.get_complex)

    def multiply(self, other):
        f = self.get_real * other.get_real
        o = self.get_real * other.get_complex
        i = self.get_complex * other.get_real
        l = self.get_complex * other.get_complex
        return complex(f + l, o + i)

    def divide(self, other):
        return complex(self.multiply(other.conjugate))

    def conjugate(self):
        return complex(self.get_real, -self.get_complex)

    def toString(self):
        return "%s + %si" % (self.get_real, self.get_complex)

    def angle(self):
        return math.atan(self.get_complex/self.get_real)
