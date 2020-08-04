"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 03/08/20
@project 
@name linear_search

"""
from random import randrange


def linear_search(item,lista):

    for index in lista:
        if index == item:
            return True
    return False

if __name__ == '__main__':
    size = int(input("Tamaño de la lista:"))
    finder = int(input("Elemento a buscar:"))
    lista = [randrange(0, size) for _ in range(size)]

    print(lista)
    print(linear_search(finder,lista))
