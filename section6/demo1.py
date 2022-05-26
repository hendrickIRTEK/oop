# Object oriented Programming
"""
OOP only work on python3
class object inherited
"""

# penggunaan class
# multi line comment mengguakan tombol ctrl + /

# class MyClass:

#     #variable
#     a = 0
#     b = 0

#     #konstruktor
#     def __init__(self):
#         # self.  (akan memanggil semua variable dan fungsi didalam kelas)
#         self.a = 5
#         self.b = 7
#         print ("kontruktor")
    
#     #dekontruktor

#     def __del__(self):
#         print ('dekontruktor')
    
#     def __str__(self):
#         return 'ini nama kelas MyClass. a =' + str(self.a) + 'b =' + str(self.b)
    
#     def say_hello(self,name):
#         print('Hello, ' + name)
    


# a = MyClass()
# print(a)
# a.say_hello('hendrick')

# Section 2 melakukan modifikasi didalam konstruktor dengan menambahkan variable
class MyClass:

    #variable
    a = 0
    b = 0

    #konstruktor
    def __init__(self, a1, b1):
        # self.  (akan memanggil semua variable dan fungsi didalam kelas)
        self.a = a1
        self.b = b1
        print ("kontruktor")
    
    #dekontruktor

    def __del__(self):
        print ('dekontruktor')
    
    def __str__(self):
        return 'ini nama kelas MyClass. a =' + str(self.a) + '.b =' + str(self.b)
    
    # fungsi fungsi
    def say_hello(self,name):
        print('Hello, ' + name)

a = MyClass(8,9)
print(a)
a.say_hello('hendrick')