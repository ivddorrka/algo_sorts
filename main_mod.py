from random import randrange
from shell_sort import shellsort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from selection_sort import selections

from generate_arrays import arrays_all

import time


def get_all_27_215_arrays(a):
    # all_sets = []
    # a = 2**7
    
    # while len(all_sets)!=9:
    arr_temp = arrays_all(a)
    # all_sets.append(arr_temp)
    # a = a*2
    return arr_temp

def time_for_selection(n):
    all_sets = get_all_27_215_arrays(n)

    Lst_main = []

    for i in range(len(all_sets)):
        tuple_prom = []
        for _ in range(5):
            start = time.time()
            work = selections(all_sets[i])
            done = time.time()
            elapsed = done-start
            tuple_prom.append(elapsed)

        Lst_main.append(sum(tuple_prom)/5)
    
    return Lst_main

def time_for_insertion(n):
    all_sets = get_all_27_215_arrays(n)
    Lst_main = []

    for i in range(len(all_sets)):
        tuple_prom = []
        for _ in range(5):
            start = time.time()
            work = insertionSort(all_sets[i])
            done = time.time()
            elapsed = done-start
            tuple_prom.append(elapsed)

        Lst_main.append(sum(tuple_prom)/5)
    
    return Lst_main

def time_for_shell(n):
    all_sets = get_all_27_215_arrays(n)
    Lst_main = []

    for i in range(len(all_sets)):
        tuple_prom = []
        for _ in range(5):
            start = time.time()
            work = shellsort(all_sets[i], len(all_sets[i]))
            done = time.time()
            elapsed = done-start
            tuple_prom.append(elapsed)

        Lst_main.append(sum(tuple_prom)/5)
    
    return Lst_main

def time_for_merge(n):
    all_sets = get_all_27_215_arrays(n)
    Lst_main = []

    for i in range(len(all_sets)):
        tuple_prom = []
        for _ in range(5):
            start = time.time()
            work = mergeSort(all_sets[i])
            done = time.time()
            elapsed = done-start
            tuple_prom.append(elapsed)

        Lst_main.append(sum(tuple_prom)/5)
    
    return Lst_main

def merge_27_215_time():

    a = 2**7 
    lst_main = []
    for _ in range(9):
        # print(a)
        for_sort = time_for_merge(a)
        for i in range(len(for_sort)):
            if i==0:
                str_here = f"Randomized, merge sort, {a} elements - average = {for_sort[i]} seconds"
            elif i==1:
                str_here = f"Upgoing, merge sort, {a} elements - average = {for_sort[i]} seconds"
            else:
                str_here = f"Downgoing, merge sort, {a} elements - average = {for_sort[i]} seconds"

            lst_main.append(str_here)
        a = a*2

    return '\n'.join(lst_main)


def shell_27_215_time():

    a = 2**7 
    lst_main = []
    for _ in range(9):
        # print(a)
        for_sort = time_for_shell(a)
        for i in range(len(for_sort)):
            if i==0:
                str_here = f"Randomized, shell sort, {a} elements - average = {for_sort[i]} seconds"
            elif i==1:
                str_here = f"Upgoing, shell sort, {a} elements - average = {for_sort[i]} seconds"
            else:
                str_here = f"Downgoing, shell sort, {a} elements - average = {for_sort[i]} seconds"

            lst_main.append(str_here)
        a = a*2

    return '\n'.join(lst_main)


def selection_27_215_time():

    a = 2**7 
    lst_main = []
    for _ in range(9):
        # print(a)
        for_sort = time_for_selection(a)
        for i in range(len(for_sort)):
            if i==0:
                str_here = f"Randomized, selection sort, {a} elements - average = {for_sort[i]} seconds"
            elif i==1:
                str_here = f"Upgoing, selection sort, {a} elements - average = {for_sort[i]} seconds"
            else:
                str_here = f"Downgoing, selection sort, {a} elements - average = {for_sort[i]} seconds"

            lst_main.append(str_here)
        a = a*2

    return '\n'.join(lst_main)


def insertion_27_215_time():

    a = 2**7 
    lst_main = []
    for _ in range(9):
        # print(a)
        for_sort = time_for_insertion(a)
        for i in range(len(for_sort)):
            if i==0:
                str_here = f"Randomized, insertion sort, {a} elements - average = {for_sort[i]} seconds"
            elif i==1:
                str_here = f"Upgoing, insertion sort, {a} elements - average = {for_sort[i]} seconds"
            else:
                str_here = f"Downgoing, insertion sort, {a} elements - average = {for_sort[i]} seconds"

            lst_main.append(str_here)
        a = a*2

    return '\n'.join(lst_main)

start_int = time.time()

a_1_str = merge_27_215_time()
a_2_str = shell_27_215_time()
a_3_str = selection_27_215_time()
a_4_str = insertion_27_215_time() 

done_1 = time.time()
result = done_1 - start_int

a_str = a_1_str + 2*'\n' + a_2_str + 2*'\n' + a_3_str + 2*'\n' + a_4_str

text_fiile = open('./average_results', "w")
n = text_fiile.write(a_str)
text_fiile.close()
print(n)
print('\n')

print(result)





