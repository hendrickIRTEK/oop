# jika satu direktori dengan program utama langsung menggunakan nama file
import mymodule
# jika tidak dalam satu folder/ atau semisal dalam subfolder maka cantumkan nama folder nya
# import mydirectory.mymodule 
import simpleadvmodule
a = mymodule.jumlah(10, 5)
print (a)

b = mymodule.kali(4, 3)
print (b)

c = simpleadvmodule.City ('Jakarta', 10, 6)
d = simpleadvmodule.City('Depok', 7, 6)
print (c)
print (d)

e = d.distance(c)
print (e)