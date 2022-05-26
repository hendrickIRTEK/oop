
import math

class shape:
    def __init__(self):
        print ('call __init__ from shape class')

    def foo(self):
        print('calling foo() from shape class')

class circle(shape):
    def __init__(self, r):
        self.r = r
    
    def calculate_area_circle(self):
        return math.pi * self.r * self.r

class rectangle(shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area_rectangle(self):
        return self.l * self.w

# Lets test the class

a = shape()
a.foo()

b = circle(5)
b.foo()
area = b.calculate_area_circle()
print('area circle : ', area)

c = rectangle(2, 3)
area = c.calculate_area_rectangle()
print('area rectangle = ', area)
