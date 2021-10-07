def insertionSort(arr):
    comp = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        current_c = 0
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                current_c += 1
        comp += current_c
        if current_c ==0:
            comp += 1 
        arr[j+1] = key
    return comp
  