import sys
def selections(A):
    for i in range(len(A)):
        
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]
    
    # Driver code to test above
    return A

print ("Sorted array")
print(selections([4, 2, 1, 4, 6, 4, 3, 2, 1]))