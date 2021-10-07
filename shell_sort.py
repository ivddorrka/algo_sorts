def shellsort(arr, n):
    comp = 0
    h = n // 2
    while h > 0:
        for i in range(h, n):
            current_c=0
            t = arr[i]
            j = i
            while j >= h and arr[j - h] > t:
                current_c += 1
                arr[j] = arr[j - h]
                j -= h
            comp += current_c

            if current_c == 0:
                comp +=1
 
            arr[j] = t
        h = h // 2
    return comp
 