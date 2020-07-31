#!/usr/bin/env python3
# Crear una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8]
# usar sentencia for para recorrer la lista
for i in lista:
    print(i)  # imprimir por consola
i = 0
while i < len(lista):
    print(lista[i] * 10)
    i += 1;
