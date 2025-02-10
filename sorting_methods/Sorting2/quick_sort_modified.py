import random
#to modify find the mid (low + high //2) then swap mid and low
def ModQuickR(A, low, high):
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
    ModQuickR(A, low, piviotindex - 1)
    ModQuickR(A, piviotindex + 1, high)
    return A
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(0, value))
    return RandList
def main():
    lis = [4,2,3,2,0,7,6,5]
    print(lis)
    print(ModQuickR(lis, 0, 7))
main()