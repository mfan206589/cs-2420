A = [10, 23, 16, 5, 8, 9, 1, 9, 20, 13, 15, 21]
def Bubble_sort(set):
    numb = len(set)
    changed = True
    while changed == True:
        changed = False      
        for i in range(0, numb - 1):
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
    print(set)
Bubble_sort(A)
def Bubble_sort_2(A):
    changed = True
    while changed == True:
        changed = False
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                changed = True
    print(A) 
Bubble_sort_2(A)
