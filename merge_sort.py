def mergeSort(array):
    comparisons = 0
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                comparisons += 1
                array[k] = left[i]
                i += 1
            else:
                comparisons+=1
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return comparisons



# a = [4, 2, 5, 3, 4, 65, 78, 2, 34, 5, 2, 4, 5, 6, 7, 5, 56]
# print(mergeSort(a))