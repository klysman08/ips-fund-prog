# defina aqui a sua classe Círculo

import math

PI = math.pi

class Circle:

    def __init__(self, raio):
        self.raio = raio

    def get_area(self):
        return PI * (self.raio ** 2)
    
    def get_perimetro(self):
        return 2 * PI * self.raio
    
    def get_circumference(self):
        return self.get_perimetro()
    

class Squere:
    def __init__(self, lado):
        self.lado = lado
    
    def get_area(self):
        return self.lado ** 2
    
    def get_perimetro(self):
        return 4 * self.lado