def partition(arr, l, h):
    """Partition is the same as for the recursive algorithm."""
    i = ( l - 1 )
    x = arr[h]
    for j in range(l, h):
        if   arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)
 

def quickSortIterative(arr, l, h):
    """Main function for quicksort implementation, \
        where l - starting index and h-edning index \
        To reduce the stack size, first push the indexes of smaller half. \
        Uses the insertion sort when the size reduces below an experimentally calculated threshold."""
        
 
    
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l

    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Uncomment the following to see what are h and l at every step of iteration through the arraa
        # print(f"H: {h}")
        # print(f"L: {l}")
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )

        # uncomment the following to see what is p equal to at everu step  
        # print(f"P is equal: {p}")
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
 
# EXAMPLE VARIANT #
# Uncomment to try #

# arr = [5, 3, 7, 8, 9, 0, 3, 2, 2, 1, 4, 0, 4, 2, 56]
# n = len(arr)
# quickSortIterative(arr, 0, n-1)
# print ("Sorted array is:")
# print(arr)

# THE OUTPUT FOR THE EXAMPLE [0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8, 9, 56] #