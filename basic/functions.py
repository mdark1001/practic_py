#!/usr/bin/env python3

#funcion recursiva de factorial
def factorial_recursiva(x):
    if x==1:
        return 1;
    else:
        return fibo_recursiva(x-1)*x
#funcion  de factorial lineal
def factorial_normal(x):
    result=1;
    while x>=1:
        result*=x;
        x=x-1;
    return result;
#function para crear el reverse de un string
def reversed_string(a_string):
    return a_string[::-1]

#funcion que determina si una cadena de texto es palindromo
def palindromo(str_palindrimo):

    str_palindrimo=str_palindrimo.replace(' ','').lower();
    str_reverse=reversed_string(str_palindrimo)
    if str_palindrimo==str_reverse:
        return 'SI'
    return 'NO'

def fibox(x):
    a=0
    b=1
    lista_fibo=[];
    lista_fibo.append(a)
    lista_fibo.append(b);
    i=1;
    while i<x:
        f=a+b
        lista_fibo.append(f);
        a=b;
        b=f;
        i=i+1;
    return lista_fibo;


print(fibox(10));
