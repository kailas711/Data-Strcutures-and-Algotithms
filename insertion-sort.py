def insertsort(A):
    """
    implementing insertion sort algorithm
    Args:
        A: list of elements to be sorted
    """
    for j in range(1, len(A)):
        key = A[j] # Insert A[J] into the sorted sequence
        # Insert A[j] into the sorted sequence A[0...j-1].
        i = j-1
        while i>=0 and A[i]>key:
            A[ i + 1 ] = A[i]
            i = i-1
        A[ i + 1 ] = key
    return A

print(insertsort([3,6,9,1,0]))