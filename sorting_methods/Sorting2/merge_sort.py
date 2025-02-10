import random
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
    rand = CreateRandom(25)
    print('Original List')
    print(rand)
    print('Sorted List')
    print(merge_sort(rand))
main()
