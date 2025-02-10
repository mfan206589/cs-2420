import random
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
#creates random list
def CreateRandom(value):
    RandList = []
    for i in range(value):
        #adds numbers to list
        RandList.append(random.randint(0, value))
    return RandList
def main():
    #before and after
    rand = CreateRandom(20)
    print(rand)
    Bubble_sort(rand)    
main()