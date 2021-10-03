from random import randrange
# from shell_sort import shellsort
# from insertion_sort import insertionSort
# from merge_sort import mergeSort
from selection_sort import selections

from generate_arrays import arrays_all

import time


def get_all_27_215_arrays():
    all_sets = []
    a = 2**7
    
    while len(all_sets)!=9:
        arr_temp = arrays_all(a)
        all_sets.append(arr_temp)
        a = a*2
    return all_sets

def time_for_selection():
    # all_sets = get_all_27_215_arrays()

    all_sets=[([1, 4, 6, 2, 3, 1, 9, 0, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1])]

    # start = time.time()
    Lst_main = []
    for i in range(len(all_sets)):
        for j in range(len(all_sets[i])):
            start = time.time()
            srt = selections(all_sets[i][j])
            done = time.time()
            elapsed = done - start
            if i==0:
                str_time_num = f"Selection sort of a random array with {len(all_sets[i][j])} elements takes {elapsed} seconds"
            elif i==1:
                str_time_num = f"Selection sort of an upgoing array with {len(all_sets[i][j])} elements takes {elapsed} seconds"
            else:
                str_time_num = f"Selection sort of an downgoing array with {len(all_sets[i][j])} elements takes {elapsed} seconds"

            Lst_main.append(str_time_num)

    return "\n".join(Lst_main)



print(time_for_selection())