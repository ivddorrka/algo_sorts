from array import array
from random import *

def arrays_all(n):
    lst1 = gen_random_array(n)
    lst2 = get_upgoing_array(n)
    lst3 = get_down_going(n)
    return lst1, lst2, lst3
    


def gen_random_array(n):
    array_1 = []
    possible_numbers = [1, 2, 3]
    for i in range(n):
        array_1.append(randrange(n))
    return array_1


def get_upgoing_array(n):
    array_1 = []
    for i in range(n):
        array_1.append(i)
        i += 1
    return array_1

def get_down_going(n):
    array_up = get_upgoing_array(n)
    return array_up[::-1]


# print(gen_random_array(10))
# print(get_upgoing_array(10))
# print(get_down_going(10))

print(arrays_all(10))