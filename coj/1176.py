"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 31/07/20
@project 
@name 1176

"""
import sys


def base3(number):
    list = ""
    while number > 0:
        mod = int(number % 3)
        number = int(number / 3)
        list += "{}".format(mod)
    return list[::-1]


def solve():
    while True:
        n = int(input())
        if n < 0:
            sys.exit()
        print(base3(n))


if __name__ == '__main__':
    solve()
