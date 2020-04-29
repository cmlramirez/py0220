from fibonacci import *

n=int(input("Por favor indique hasta qué número generar: "))

l=[1]

for x in range(2, n + 1) :
    l.append(fibo(x))

print(l)
