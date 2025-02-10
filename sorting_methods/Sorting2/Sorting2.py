import random
def QuickR(A, low, high):
    if high - low <= 0:
        return
    #partition
    piviot = A[low]
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if A[i] < piviot:
            A[i] , A[lmgt] = A[lmgt] , A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[low] , A[piviotindex] = A[piviotindex] , A[low]
    #recursive step
    QuickR(A, low, piviotindex - 1)
    QuickR(A, piviotindex + 1, high)
    return A
def ModQuickR(A, low, high):
    if low < high:    
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]
        
        pivot = A[low] 
        lmgt = low + 1 
        
        # Partition
        for i in range(low + 1, high + 1):
            if A[i] < pivot:
                A[i], A[lmgt] = A[lmgt], A[i] 
                lmgt += 1
        
        pivot_index = lmgt - 1
        A[low], A[pivot_index] = A[pivot_index], A[low]

        ModQuickR(A, low, pivot_index - 1)
        ModQuickR(A, pivot_index + 1, high)
    
    return A
def merge_sort(A):
    if len(A) <= 1:
        return A
    #splits the list
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    #splits the already splited peices
    #recursion
    left = merge_sort(left)
    right = merge_sort(right)
    
    i = j = k = 0
    #attempts to sort the lists and re-combines them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        A[k] = right[j]
        j = j + 1
        k = k + 1 
    return A
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(1, 100))
    return RandList
def main():
    randlist = CreateRandom(20)
    lis = [4,2,3,2,0,7,6,5]
    print("Merge Sort:")
    print(merge_sort(randlist))
    print("Quick Sort:")
    print(QuickR(lis[:], 0, 7))
    print("Quick Sort Modified:")
    print(ModQuickR(lis, 0, 7))
main()