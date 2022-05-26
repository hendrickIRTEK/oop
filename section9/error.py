# raise error

try:
    a = 8
    b = 0

    c = a/b
    print('result', str(c))

#use this if you didnt know the error
except Exception as e:
    print (e)
# except ZeroDivisionError as e:
#     print('Error: devision by zero')
#     print (e)

finally:
    print ('Done')

print('exit from program')