"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 03/08/20
@project 
@name bubble_sort

"""
from random import  randrange


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    size = int(input("Tamaño de la lista:"))

    lista = [randrange(0, size) for _ in range(size)]
    # ordernar la lista
    print(lista)
    lista = bubble_sort(lista)
    print(lista)
