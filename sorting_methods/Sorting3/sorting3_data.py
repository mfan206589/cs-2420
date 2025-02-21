import sys
import random
import math
sys.setrecursionlimit(10000)
def bubble(set, count):
    changed = True
    # Loop until no more changes are made
    while changed:
        changed = False
        # Traverse the list from left to right
        for i in range(0, len(set) - 1):
            count[0] += 1
            # Swap if the current element is greater than the next element
            if set[i] > set[i + 1]:
                set[i], set[i + 1] = set[i + 1], set[i]
                changed = True

def shaker(set, count):
    changed = True
    # Loop until no more changes are made
    while changed:
        changed = False
        # Traverse the list from left to right
        for i in range(0, len(set) - 1):
            count[0] += 1
            # Swap if the current element is greater than the next element
            if set[i] > set[i + 1]:
                set[i], set[i + 1] = set[i + 1], set[i]
                changed = True  
        # Traverse the list from right to left
        for i in range(len(set) - 2, -1, -1):
            count[0] += 1
            # Swap if the current element is greater than the next element
            if set[i] > set[i + 1]:
                set[i], set[i + 1] = set[i + 1], set[i]
                changed = True

def counting(A, count):
    # Create a frequency array
    F = [0] * (max(A) + 1)
    for i in A:
        F[i] += 1
    k = 0
    # Reconstruct the sorted array
    for s in range(len(F)):
        count[0] += F[s]  # Counting comparisons
        for j in range(F[s]):
            A[k] = s
            k += 1

def merge(A, count):
    if len(A) <= 1:
        return A
    # Split the list into two halves
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    # Recursively split and merge the halves
    left = merge(left, count)
    right = merge(right, count)
   
    i = j = k = 0
    # Merge the sorted halves
    while i < len(left) and j < len(right):
        count[0] += 1
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    return A

def quick(A, low, high, count):
    count[0] += 1
    if high - low <= 0:
        return
    # Partition the list
    piviot = A[low]
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        count[0] += 1
        if A[i] < piviot:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[low], A[piviotindex] = A[piviotindex], A[low]
    # Recursively sort the partitions
    quick(A, low, piviotindex - 1, count)
    quick(A, piviotindex + 1, high, count)
    return A

def quickmodified(A, low, high, count):
    F = []
    for i in range(len(A)):
        count[0] += 1
        F.append(0)
    if high - low <= 0:
        return
    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]
    # Partition the list
    piviot = A[mid]
    lmgt = mid + 1
    for i in range(mid + 1, high + 1):
        count[0] += 1
        if A[i] < piviot:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[mid], A[piviotindex] = A[piviotindex], A[mid]
    # Recursively sort the partitions
    quickmodified(A, low, piviotindex - 1, count)
    quickmodified(A, piviotindex + 1, high, count)
    return A

def CreateRandom(value):
    RandList = []
    for i in range(value):
        # Add random numbers to the list
        RandList.append(random.randint(0, value))
    return RandList

def create_mostly_sorted(size):
    sortedlist = CreateRandom(size)
    sortedlist.sort()
    # Swap the first and last elements to make it mostly sorted
    sortedlist[0], sortedlist[-1] = sortedlist[-1], sortedlist[0]
    return sortedlist

def main():
    print('Random Data Set Comparison')
    print('Size: Bubble  Shaker  Counting  Merge  Quick  QuickMod')
    algorithms = [bubble, shaker, counting, merge, quick, quickmodified]
    for s in range(3, 12 + 1):
        size = 2 ** s
        print(s, end=" ")
        for sort in algorithms:
            A = CreateRandom(size)
            count = [0]
            if sort in [quick, quickmodified]:
                sort(A, 0, len(A) - 1, count)
            else:
                sort(A, count)
            if count[0] > 0:
                print(f"{math.log(count[0], 2):>8.2f}", end=" ")
        print()
    print('Mostly Sorted Data Set Comparison')
    print('Size: Bubble  Shaker  Counting  Merge  Quick  QuickMod')
    algorithms = [bubble, shaker, counting, merge, quick, quickmodified]
    for s in range(3, 12 + 1):
        size = 2 ** s
        print(s, end=" ")
        for sort in algorithms:
            A = create_mostly_sorted(size)
            count = [0]
            if sort in [quick, quickmodified]:
                sort(A, 0, len(A) - 1, count)
            else:
                sort(A, count)
            if count[0] > 0:
                print(f"{math.log(count[0], 2):>8.2f}", end=" ")
        print()

# Run the main function
main()