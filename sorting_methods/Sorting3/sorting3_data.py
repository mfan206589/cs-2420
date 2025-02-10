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
        #This checks the data from right to left    
        for i in range(len(set) - 2, -1, -1):
                #checks to see if number is bigger if so switches the two numbers
                count[0] += 1
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
def counting(A, count):
    F = []
    #or F = [0]*len(A)
    #Create the frequency list
    for a in range(len(A)):
        F.append(0)
    for i in A:
        F[i] += 1
    k = 0
    for s in range(len(A)):
       count = F[s]
       value = s
       for j in range(count):
           A[k] = value
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
    left = merge(left)
    right = merge(right)
    
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
def quick(A, low, high, count):
    F = []
    for i in range(len(A)):
        count[0]+1
        F.append(0)
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
    quick(A, low, piviotindex - 1)
    quick(A, piviotindex + 1, high)
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
        if A[i] < piviot:
            A[i] , A[lmgt] = A[lmgt] , A[i]
            lmgt += 1
    piviotindex = lmgt - 1
    A[mid] , A[piviotindex] = A[piviotindex] , A[mid]
    #recursive step
    quickmodified(A, low, piviotindex - 1)
    quickmodified(A, piviotindex + 1, high)
    return A
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(0, value))
    return RandList
def main():
    algorithms = [bubble, shaker, counting, merge, quick, quickmodified]
    for s in range(3, 12+1):
        size = 2 ** s
        print(s, end=" ")
        for sort in algorithms:
            A = CreateRandom(size)
            B = A[:]
            count = [0]
            sort(A, count)
            if(A!=B):
                print('Error!')
            print(math.log(count[0], 2),end=" ")
        print()
main()