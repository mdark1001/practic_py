"""

@description: calcular pi usando la formula de Leinbiz, que es una serie de numeros tal que

pi = 4/1 + 4/3 - 4/5 + 4/7 ...

tomando en cuenta que el numerador es una constante (4)
y el denominador iniciando en 1 e incrementando en 2
también considere la alternación del signo + -

"""

from functools import lru_cache
import sys
import time


def calculate_pi_recursivo(numbers, pi, denominador, operador):
    """
        implementación recursiva de la serie de Leinbiz para calcular pi
    """
    if numbers == 1:
        return pi
    pi += operador * (4 / denominador)
    return calculate_pi_recursivo(numbers - 1, pi, denominador + 2, operador * -1)


def calculate_pi(numbers):
    """
        implementación iterativa de la serie de Leinbiz
    """

    pi = 0.0
    numerador = 4
    denominador = 1
    operador = 1
    for _ in range(numbers):
        pi += operador * (numerador / denominador)
        denominador += 2
        operador *= -1  # es una forma de intercambiar entre la operacion + -
    return pi


if __name__ == '__main__':
    numbers = 10000
    inicio = time.time()
    print(calculate_pi(numbers))
    final = time.time()
    print(final - inicio)

    sys.setrecursionlimit(10000000)  # para la implemtación recursiva
    inicio = time.time()
    print(calculate_pi_recursivo(numbers, 0, 1, 1))
    final = time.time()
    print(final - inicio)
