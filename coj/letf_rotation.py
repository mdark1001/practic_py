"""
@author mdark1001 --> Miguel Cabrera R. <miguel.cabrera.app@gmail.com>   
@date 04/08/20
@project 
@name letf_rotation

"""


def rotleft(a, d):
    a2 = a[0:d]
    a = a[d:] + a2
    return a


if __name__ == '__main__':

    print(rotleft([41, 73,  89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10))
