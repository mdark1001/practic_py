"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 03/08/20
@project 
@name merge_sort

"""
from random import randrange


def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierdo = lista[:medio]
        derecho = lista[medio:]

        ## llamada recursiva en cada mitad
        merge_sort(izquierdo)
        merge_sort(derecho)
        # init vars
        i = 0
        j = 0
        # K para iterador de lista
        k = 0
        while i < len(izquierdo) and j < len(derecho):
            if izquierdo[i] < derecho[j]:
                lista[k] = izquierdo[i]
                i += 1
            else:
                lista[k] = derecho[j]
                j += 1
            k += 1
        while i < len(izquierdo):
            lista[k] = izquierdo[i]
            i += 1
            k += 1
        while j < len(derecho):
            lista[k] = derecho[j]
            j += 1
            k += 1
    return lista

if __name__ == '__main__':
    size = int(input("Tamaño de la lista:"))

    lista = [randrange(0, size) for _ in range(size)]
    # ordernar la lista
    print(lista)
    lista = merge_sort(lista)
    print(lista)
