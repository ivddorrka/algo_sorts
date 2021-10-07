from array import array
from random import *

def arrays_all(n):
    lst1 = gen_random_array(n)
    lst2 = get_upgoing_array(n)
    lst3 = get_down_going(n)
    return lst1, lst2, lst3
    
def get_random_123_array(n):
    lst = []
    for i in range(n):
        a = randint(1,3)
        lst.append(a)
    return lst

# print(get_random_123_array(9))


def gen_random_array(n):
    array_1 = []
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


def generate_5_ran(n):
    lst = []
    for i in range(5):
        a = gen_random_array(n)
        lst.append(a)
    return lst

def get_5_123_arrays(n):
    lst = []
    for i in range(5):
        a = get_random_123_array(n)
        lst.append(a)
    return lst


def get_two_ran_lsts(n):
    a = generate_5_ran(n)
    b = get_5_123_arrays(n)
    return [a, b]

# a = get_random_123_array(54)
# print(a)