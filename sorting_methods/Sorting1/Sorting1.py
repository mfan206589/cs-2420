import random
#better for sorted data
#creates random set of numbers
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to a list
        RandList.append(random.randint(1, 100))
    return RandList
def Shaker_sort(set):
    changed = True
    #checks to see if numbers have switched
    while changed:
        #Starts the while loop
        changed = False
        #Begins to read list from left to right     
        for i in range(0, len(set) - 1):
                #checks if numbers are bigger if so switches them
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
        #This checks the data from right to left    
        for i in range(len(set) - 2, -1, -1):
                #checks to see if number is bigger if so switches the two numbers
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
    print(set)
#Similar to shaker just reads left to right instead
#better for random list with no sorting
def Bubble_sort(set):
    changed = True
    #defines loop
    while changed:
        #starts loop
        changed = False 
        #Begins to read list from left to right     
        for i in range(0, len(set) - 1):
                #checks if numbers are bigger if so switches them
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
    print(set)
def Random_Seven():
    rand_s_list = []
    for i in range(8):
        rand_s_list.append(random.randint(0, 7))
    return rand_s_list
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
    print('Bubble Sort Method')
    Bubble_sort(CreateRandom(20))
    print('Shaker Sort Method')
    Shaker_sort(CreateRandom(20))
    s_rand = Random_Seven()
    print('Counting Sort Method')
    Counting_sort(s_rand)
main()