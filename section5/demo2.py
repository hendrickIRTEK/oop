# rukursif
# fungsi yang di panggil didalam fungsi




def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

val = fibonacci(10)
print(val)
