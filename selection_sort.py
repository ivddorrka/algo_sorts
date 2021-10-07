def selections(A):
    comp = 0
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
            comp += 1
     
        A[i], A[min_idx] = A[min_idx], A[i]
    
    return comp
