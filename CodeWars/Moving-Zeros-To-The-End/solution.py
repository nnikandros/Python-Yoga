def move_zeros(lst):
    n = len(lst)
    j = 0
    for i in range(n):
        if lst[i] != 0:
            lst[j], lst[i] = lst[i], lst[j]  # Partitioning the array
            j += 1
    return lst  # Print 


#### more pythonic solution

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
