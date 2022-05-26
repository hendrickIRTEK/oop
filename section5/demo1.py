# fungsi
# untuk membuat fungsi menggunakan Def

def hello():
    # do something
    print('hello')

def foo():
    pass

def hitung_jumlah(a,b):
    # do something
    return a+b    

def say_hello(name):
    print('Hello, ' + name)

def ambil_data():
    return 10
# input 2 jenis output kendali 3
def calculate(a,b):
    return a+b,a-b,a*b    


hello()
c = hitung_jumlah(10,5)
print(c)
say_hello('agus')
print(ambil_data())

val = calculate(10,7)
print(val)
a,b,c = calculate(5,8)
print(a)
print(b)
print(c)
#ambil nilai b saja
_,b,_ = calculate(5,8)
print(b)