def shellsort(arr, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = arr[i]
            j = i
            while j >= h and arr[j - h] > t:
                arr[j] = arr[j - h]
                j -= h
 
            arr[j] = t
        h = h // 2
    return arr
 
 
inp = [9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
n = len(inp)
# print('Array before Sorting:')
# print(inp)
# shell_sort(inp, n)
# print('Array after Sorting:')
# print(inp)

print(shellsort(inp, n))