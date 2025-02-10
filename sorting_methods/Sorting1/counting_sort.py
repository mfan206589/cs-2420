A = [6,2,3,7,3,4,7,2]
#counts how many times a number occures
def Counting_sort(A):
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
    print(A)
    print(F)
def main():
    Counting_sort(A)
main()