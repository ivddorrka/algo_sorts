from random import randrange
from shell_sort import shellsort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from selection_sort import selections

from generate_arrays import gen_random_array, get_upgoing_array, get_down_going, get_two_ran_lsts
import copy
import time

def time_for_selection(lst_1, n):
    mas_upgoing = get_upgoing_array(n)
    str_times = ""
    time_1 = time.time()
    comp_1 = selections(mas_upgoing)
    done_1 = time.time()
    elapsed_1 = done_1 - time_1
    str_times +=  f"Time for an upgoing array is {elapsed_1} seconds for {n} elements for selection sort with {comp_1} comparisons"
    mas_descending = get_down_going(n)
    time_2 = time.time()
    comp_2 = selections(mas_descending)
    done_2 = time.time()
    elapsed_2 = done_2 - time_2
    str_times +='\n'
    str_times +=  f"Time for a descending array is {elapsed_2} seconds for {n} elements for selection sort with {comp_2} comparisons"
    time_random_av = 0
    comp_3 = 0
    for i in range(len(lst_1[0])):
        a = lst_1[0][i]
        time_3 = time.time()
        comp_3 +=selections(a)
        done_3 = time.time()
        time_random_av += (done_3 - time_3)

    str_times +='\n'
    elapsed_3 =  time_random_av/5
    str_times +=  f"Time for a random array is {elapsed_3} seconds for {n} elements for selection sort with {int(comp_3/5)} comparisons"
    comp_4 = 0
    time_random_av1 = []
    for j in range(len(lst_1[1])):
        b = lst_1[1][j]
        time_4 = time.time()
        comp_4 += selections(b)
        done_4 = time.time()
        time_random_av1.append((done_4 - time_4))

    str_times +='\n'
    elapsed_4 =  sum(time_random_av1)/(len(lst_1[1]))
    str_times +=  f"Time for a random array is {elapsed_4} seconds for {n} elements for selection sort if all elements are 1, 2 or 3 with {int(comp_4/5)} comparisons"


    return str_times


def time_for_merge(lst_1, n):
    mas_upgoing = get_upgoing_array(n)
    str_times = ""
    time_1 = time.time()
    comp_1 = mergeSort(mas_upgoing)
    
    done_1 = time.time()
    elapsed_1 = done_1 - time_1
    str_times +=  f"Time for an upgoing array is {elapsed_1} seconds for {n} elements for merge sort with {comp_1} comparisons"
    mas_descending = get_down_going(n)
    time_2 = time.time()
    comp_2 = mergeSort(mas_descending)
    done_2 = time.time()
    elapsed_2 = done_2 - time_2
    str_times +='\n'
    str_times +=  f"Time for a descending array is {elapsed_2} seconds for {n} elements for merge sort with {comp_2} comparisons "
    time_random_av = 0
    comp_3 = 0
    for i in range(len(lst_1[0])):
        a = lst_1[0][i]
        time_3 = time.time()
        comp_3 += mergeSort(a)
        done_3 = time.time()
        time_random_av += (done_3 - time_3)

    str_times +='\n'
    elapsed_3 =  time_random_av/5
    str_times +=  f"Time for a random array is {elapsed_3} seconds for {n} elements for merge sort with {int(comp_3/5)} comparisons"

    time_random_av1 = []
    comp_4 = 0
    for j in range(len(lst_1[1])):
        b = lst_1[1][j]
        time_4 = time.time()
        comp_4 += mergeSort(b)
        done_4 = time.time()
        time_random_av1.append((done_4 - time_4))

    str_times +='\n'
    elapsed_4 =  sum(time_random_av1)/(len(lst_1[1]))
    str_times +=  f"Time for a random array is {elapsed_4} seconds for {n} elements for merge sort if all elements are 1, 2 or 3 with {int(comp_4/5)} comparisons"


    return str_times

def time_for_shell(lst_1, n):
    mas_upgoing = get_upgoing_array(n)
    str_times = ""
    time_1 = time.time()
    comp_1=shellsort(mas_upgoing, len(mas_upgoing))
    done_1 = time.time()
    elapsed_1 = done_1 - time_1
    str_times +=  f"Time for an upgoing array is {elapsed_1} seconds for {n} elements for shell sort with {comp_1} comparisons"
    mas_descending = get_down_going(n)
    time_2 = time.time()
    comp_2=shellsort(mas_descending, len(mas_descending))
    done_2 = time.time()
    elapsed_2 = done_2 - time_2
    str_times +='\n'
    str_times +=  f"Time for a descending array is {elapsed_2} seconds for {n} elements for shell sort with {comp_2} comparisons"
    time_random_av = 0
    comp_3=0
    for i in range(len(lst_1[0])):
        a = lst_1[0][i]
        time_3 = time.time()
        comp_3 += shellsort(a, len(a))
        done_3 = time.time()
        time_random_av += (done_3 - time_3)

    str_times +='\n'
    elapsed_3 =  time_random_av/5
    str_times +=  f"Time for a random array is {elapsed_3} seconds for {n} elements for shell sort with {int(comp_3/5)} comparisons"

    time_random_av1 = []
    comp_4=0
    for j in range(len(lst_1[1])):
        b = lst_1[1][j]
        time_4 = time.time()
        comp_4 += shellsort(b, len(b))
        done_4 = time.time()
        time_random_av1.append((done_4 - time_4))

    str_times +='\n'
    elapsed_4 =  sum(time_random_av1)/(len(lst_1[1]))
    str_times +=  f"Time for a random array is {elapsed_4} seconds for {n} elements for shell sort if all elements are 1, 2 or 3 with {int(comp_4/5)} comparisons"
    
    return str_times

def time_for_insertion(lst_1, n):
    mas_upgoing = get_upgoing_array(n)
    str_times = ""
    time_1 = time.time()
    comp_1=insertionSort(mas_upgoing)
    done_1 = time.time()
    elapsed_1 = done_1 - time_1
    str_times +=  f"Time for an upgoing array is {elapsed_1} seconds for {n} elements for insertion sort with {comp_1} comparisons"
    mas_descending = get_down_going(n)
    time_2 = time.time()
    comp_2=insertionSort(mas_descending)
    done_2 = time.time()
    elapsed_2 = done_2 - time_2
    str_times +='\n'
    str_times +=  f"Time for a descending array is {elapsed_2} seconds for {n} elements for insertion sort with {comp_2} comparisons"
    time_random_av = 0
    comp_3=0
    for i in range(len(lst_1[0])):
        a = lst_1[0][i]
        time_3 = time.time()
        comp_3 += insertionSort(a)
        done_3 = time.time()
        time_random_av += (done_3 - time_3)

    str_times +='\n'
    elapsed_3 =  time_random_av/5
    str_times +=  f"Time for a random array is {elapsed_3} seconds for {n} elements for insertion sort with {int(comp_3/5)} comparisons"

    
    time_random_av1 = []
    comp_4=0
    for j in range(len(lst_1[1])):
        b = lst_1[1][j]
        time_4 = time.time()
        comp_4 += insertionSort(b)
        done_4 = time.time()
        time_random_av1.append((done_4 - time_4))

    str_times +='\n'
    elapsed_4 =  sum(time_random_av1)/(len(lst_1[1]))
    str_times +=  f"Time for a random array is {elapsed_4} seconds for {n} elements for insertion sort if all elements are 1, 2 or 3  with {int(comp_4/5)} comparisons"

    return str_times

         
# print(time_for_selection(57))
n = 2**15
lst = get_two_ran_lsts(n)

b = copy.deepcopy(lst)
c = copy.deepcopy(lst)
d = copy.deepcopy(lst)
h = copy.deepcopy(lst)

print(time_for_selection(b, n))
print(time_for_insertion(c, n))
print(time_for_merge(d, n))
print(time_for_shell(h, n))

# a = [3, 2, 2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 1, 3, 1, 2, 3, 1, 3, 1, 1, 2, 3, 3, 3, 1, 2, 3, 3, 1, 1, 2]
# a = [1, 2, 3, 4]
# start = time.time()
# mergeSort(a)
# done = time.time()
# eplsj = done - start
# print(eplsj)