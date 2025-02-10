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
        #This checks the data from right to left    
        for i in range(len(set) - 2, -1, -1):
                #checks to see if number is bigger if so switches the two numbers
                if set[i] > set[i + 1]:
                    set[i], set[i + 1] = set[i + 1], set[i]
                    changed = True
        print(set)
def main():
    #creates the random list and prints the before and after
    rand = CreateRandom(20)
    print(rand)
    Shaker_sort(rand)
main()