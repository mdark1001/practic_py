#!/usr/bin/env python3

# funcion recursiva de factorial
def factorial_recursiva(x):
    if x == 1:
        return 1
    else:
        return factorial_recursiva(x - 1) * x


# funcion  de factorial lineal o iterativo
def factorial_iterativo(x):
    result = 1
    while x >= 1:
        result *= x;
        x = x - 1;
    return result;


# function para crear el reverse de un string
def reversed_string(a_string):
    return a_string[::-1]


# funcion que determina si una cadena de texto es palindromo
def palindromo(str_palindrimo):
    str_palindrimo = str_palindrimo.replace(' ', '').lower();
    str_reverse = reversed_string(str_palindrimo)
    if str_palindrimo == str_reverse:
        return 'SI'
    return 'NO'


if __name__ == '__main__':
    print(factorial_recursiva(5))
    print(factorial_iterativo(5))