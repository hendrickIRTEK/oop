class Parent:
    def say_hello(self):
        print('Hello from Parent')

# dengan format seperti ini maka child akan mendapat semua fitur yang ada di parent
class Child (Parent):
    def say_thanks(self):
        print ('Hello from child')


# Lets test the program
a = Parent()
b = Child()
a.say_hello()
b.say_hello()
b.say_thanks()