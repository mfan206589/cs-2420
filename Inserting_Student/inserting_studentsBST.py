import time
from pathlib import Path

# Define file paths
root_dir = Path(__file__).parent
Fake = root_dir / 'FakeNames.txt'
Retrieve = root_dir / 'RetrieveNames.txt'
Delete = root_dir / 'DeleteNames.txt'

# Define the Student class
class Student:
    def __init__(self, ln, fn, ssn, email, age):
        self.ln = ln
        self.fn = fn
        self.ssn = ssn
        self.email = email
        self.age = age

    def __eq__(self, rhs):
        return self.ssn == rhs.ssn
class Node:
    def __init__(self, item):
        self.item = item
        self.L = None
        self.R = None
# Define the Bag class to manage a collection of students
class Bag:
    def __init__(self):
        self.root = None
    def Insert(self, item):
        if self.Exists(item):
            return False
        self.root = self.InsertR(item, self.root)
        return True
    def InsertR(self, item, current):
        if current is None:
            current = Node(item)
        elif item < current.item.ssn:
            current.L = self.InsertR(item, current.L)
        else:
            current.R = self.InsertR(item, current.R)
        return current
    def Retrive(self, item):
        return self.RetriveR(item, self.root)
    def RetriveR(self, item, current):
        if current is None:
            return None
        if item == current.item.ssn:
            return current.item
        elif item < current.item.ssn:
            return self.RetriveR(item, current.L)
        else:
            return self.RetriveR(item, current.R)
    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.root = self.DeleteR(item, self.root)
        return True
    def DeleteR(self, item, current):
        if item < current.item.ssn:
            current.L = self.DeleteR(item, current.L)
        elif item > current.item.ssn:
            current.R =  self.DeleteR(item, current.R)
        else:
            if current.L is None and current.R is None:
                current = None
            elif current.R:
                current = current.R 
            elif current.L:
                current = current.L
            else:
                succsessor = current.R
                while succsessor.L:
                    succsessor = succsessor.L
                current.item.ssn = succsessor.item.ssn
                current.R = self.DeleteR(succsessor.item.ssn, current.R)
        return current
    def Exists(self, item):
        return self.ExistsR(item, self.root)
    def ExistsR(self, item, current):
        if current is None:
            return False
        if item == current.item.ssn:
            return True
        elif item < current.item.ssn:
            return self.ExistsR(item, current.L)
        else:
            return self.ExistsR(item, current.R)
    def Size(self):
        return self.SizeR(self.root)
    def SizeR(self, current):
        return 1 + self.SizeR(current.L)
    def __iter__(self):
        yield from self.IterR(self.root)
    def IterR(self, current):
        if current is not None:
            yield from self.IterR(current.left)
            yield current.item
            yield from self.IterR(current.right)

# Main function to execute the program
def main():
    t1 = time.time()  # Start timing
    bag = Bag()  # Create a new Bag instance
    TotalFails = 0
    # Insert students from FakeNames.txt
    with open(Fake, 'r') as file:
        for line in file:
            data = line.strip().split()
            ln, fn, ssn, email, age = data
            student = Student(ln, fn, ssn, email, int(age))
            if not bag.Insert(student):
                TotalFails += 1

    t2 = time.time()  # Time after inserting students
    t3 = time.time()  # Start timing for retrieval

    # Retrieve students from RetrieveNames.txt and calculate average age
    with open(Retrieve, 'r') as file2:
        retrieved = []
        total_age = 0
        total_people = 0
        for line in file2:
            retrieve_ssn = line.strip()
            retrieved.append(retrieve_ssn)
        for ssn in retrieved:
            person = bag.Retrive(ssn)
            if person:
                total_age += person.age
                total_people += 1
            else:
                TotalFails += 1
        average = round(total_age / total_people, 5)  # Calculate average age

    t4 = time.time()  # Time after retrieval
    t5 = time.time()  # Start timing for deletion

    # Delete students from DeleteNames.txt
    with open(Delete, 'r') as file3:
        for line in file3:
            person = bag.Delete(line.strip())
            if person:
                pass
            else:
                TotalFails += 1

    t6 = time.time()  # Time after deletion

    # Print results
    print(f'Total Number of Fails: {TotalFails}')
    print(f'Total Number of Students: {bag.Size()}')
    print(f'Time Took to Total: {t2 - t1}')
    print(f'Average Age of Retrieved Students: {average}')
    print(f'Time Took to Average: {t4 - t3}')
    print(f'Time Took to Delete Students: {t6 - t5}')

# Run the main function
main()