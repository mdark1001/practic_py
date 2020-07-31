"""

fibonacci implemtación de en python usando recursividad,lineal y usando los generadores

@description: The Fibonacci sequence is a sequence of numbers such that any number, except for the first and second, is the sum of the previous two:

0 1 1 2 3 5 8...
suma del numero anterior excepto los 2 primeros
"""
import typing
from typing import Dict


# fibo usando los casos base

def fibo2(number):
    """
    Es un llamado recursivo, para calcular el numero fibonacci,
    de 4 es necesario ejecutar (llamar la funcion) 9 veces
    fibo2(4) -> 9
    fibo2(5)  -> 175
    fibo2(20) -> 891
    """
    if number < 2:
        return number
    return fibo2(number - 1) + fibo2(number - 2)


# usando la tecnica de memorización,
# podemos agregar un diccionario para guardar los resultados de una llamada de fibo


fibo_result: Dict[int, int] = {0: 0, 1: 1}


def fibo3(number):
    """
    si ahora ejecutamos el fibo3(50) obtendremos sin problema el resultado
    """
    if not number in fibo_result:
        fibo_result[number] = fibo3(number - 1) + fibo3(number - 2)  # usando la memoria
    return fibo_result[number]


# usando la caché como tecnica de memorizacion

from functools import lru_cache


# usando como decorador:

@lru_cache(maxsize=None)
def fibo4(number):
    if number < 2:
        return number
    return fibo4(number - 1) + fibo4(number - 2)


# finonacci lineal

def fibo_lineal(number):
    # any problem that can be solved recursively can also be solved iteratively.
    if number < 2:
        return number
    last = 0
    next = 1

    for _ in range(1, number):
        last, next = next, last + next
    return next


# usando los generadores de python


def fib6(n: int) -> typing.Generator[int, None, None]:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == '__main__':
    print(fibo2(20))
    print(fibo3(20))
    print(fibo4(20))
    for i in fib6(20):
        print(i)
