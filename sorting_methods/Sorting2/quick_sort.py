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
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(0, value))
    return RandList
def main():
    lis = [4,2,3,2,0,7,6,5]
    print(lis)
    print(QuickR(lis, 0, 7))
main()