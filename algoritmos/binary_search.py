"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 03/08/20
@project 
@name binary_search

"""
import random


def binary_search(item, lista, comienzo=0, final=0, couter=1):
    if comienzo > final:
        print(couter)
        return False
    medio = (comienzo + final) // 2
    couter += 1
    if lista[medio] == item:
        print(couter)
        return True
    elif lista[medio] < item:
        return binary_search(item, lista, medio + 1, final, couter)
    else:
        return binary_search(item, lista, comienzo, medio - 1, couter)


if __name__ == '__main__':
    size = int(input("Tamaño de la lista:"))
    finder = int(input("Elemento a buscar:"))
    lista = [random.randrange(0, size) for _ in range(size)]
    # ordernar la lista
    lista = sorted(lista)
    print(lista)
    print(binary_search(item=finder, lista=lista, comienzo=0, final=len(lista), couter=1))
