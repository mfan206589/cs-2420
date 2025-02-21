import sys
import random
import math
sys.setrecursionlimit(10000)
def bubble(set, count):
    changed = True
    #defines loop
    while changed:
        #starts loop
        changed = False
        #Begins to read list from left to right    
        for i in range(0, len(set) - 1):
                #checks if numbers are bigger if so switches them
                count[0] += 1
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
def shaker(set, count):
    changed = True
    #checks to see if numbers have switched
    while changed:
        #Starts the while loop
        changed = False
        for i in range(0, len(set) - 1):
                #checks if numbers are bigger if so switches them
                count[0] += 1
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True  
        #This checks the data from right to left    
        for i in range(len(set) - 2, -1, -1):
                #checks to see if number is bigger if so switches the two numbers
                count[0] += 1
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
def counting(A, count):
    F = [0] * (max(A) + 1)
    for i in A:
        F[i] += 1
    k = 0
    for s in range(len(F)):
        count[0] += F[s]  # Counting comparisons
        for j in range(F[s]):
            A[k] = s
            k += 1
def merge(A, count):
    if len(A) <= 1:
        return A
    #splits the list
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    #splits the already splited peices
    #recursion
    left = merge(left, count)
    right = merge(right, count)
   
    i = j = k = 0
    #attempts to sort the lists and re-combines them
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
        i = i + 1
        k = k + 1
    while j < len(right):
        A[k] = right[j]
        j = j + 1
        k = k + 1
    return A
def quick(A, low, high, count):
    count[0] += 1
    if high - low <= 0:
        return
    #partition
    piviot = A[low]
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        count[0] += 1
        if A[i] < piviot:
            A[i] , A[lmgt] = A[lmgt] , A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[low] , A[piviotindex] = A[piviotindex] , A[low]
    #recursive step
    quick(A, low, piviotindex - 1, count)
    quick(A, piviotindex + 1, high, count)
    return A
def quickmodified(A, low, high, count):
    F = []
    for i in range(len(A)):
        count[0]+1
        F.append(0)
    if high - low <= 0:
        return
    mid = (low + high) // 2
    A[low] , A[mid] = A[mid], A[low]
    #partition
    piviot = A[mid]
    lmgt = mid + 1
    for i in range(mid + 1, high + 1):
        count[0] += 1
        if A[i] < piviot:
            A[i] , A[lmgt] = A[lmgt] , A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[mid] , A[piviotindex] = A[piviotindex] , A[mid]
    #recursive step
    quickmodified(A, low, piviotindex - 1, count)
    quickmodified(A, piviotindex + 1, high, count)
    return A
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(0, value))
    return RandList
def create_mostly_sorted(size):
    sortedlist = CreateRandom(size)
    sortedlist.sort()
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
main()