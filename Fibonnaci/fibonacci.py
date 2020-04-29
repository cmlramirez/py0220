"""
   Módulo Fibonacci
   2020-04-22
   Greencore - PY0220
   Módulo de ejemplo con la serie de Fibonacci implementada de múltiples maneras.
"""

def fibo(n):
    # Recibe un número entero mayor a cero n, y devuelve el elemento n-ésimo de la serie de Fibonacci
    if n <= 2:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

"""
   fibo(1) -> 1
   fibo(2) -> 1
   fibo(3) -> fibo(2)+fibo(1) -> 1+1 -> 2
   fibo(4) -> fibo(3)+fibo(2) -> (fibo(2)+fibo(1))+1 -> (1+1)+1 -> 3
   fibo(5) -> fibo(4)+fibo(3) -> (fibo(3)+fibo(2))+(fibo(2)+fibo(1)) -> ((fibo(2)+fibo(1))+1)... -> 5
"""
