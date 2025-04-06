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
        if self.Exists(item.ssn):
            return False
        self.root = self.InsertR(item, self.root)
        return True

    def InsertR(self, item, current):
        if current is None:
            current = Node(item)
        elif item.ssn < current.item.ssn:
            current.L = self.InsertR(item, current.L)
        else:
            current.R = self.InsertR(item, current.R)
        return current

    def Retrieve(self, ssn):
        return self.RetrieveR(ssn, self.root)

    def RetrieveR(self, ssn, current):
        if current is None:
            return None
        if ssn == current.item.ssn:  
            return current.item
        elif ssn < current.item.ssn:
            return self.RetrieveR(ssn, current.L)
        else:
            return self.RetrieveR(ssn, current.R)

    def Delete(self, ssn):
        if not self.Exists(ssn):
            return None
        self.root, deleted_item = self.DeleteR(ssn, self.root)
        return deleted_item

    def DeleteR(self, ssn, current):
        if current is None:
            return current, None
        if ssn < current.item.ssn:
            current.L, deleted_item = self.DeleteR(ssn, current.L)
        elif ssn > current.item.ssn:
            current.R, deleted_item = self.DeleteR(ssn, current.R)
        else:
           
            deleted_item = current.item
            if current.L is None and current.R is None:  
                current = None
            elif current.R:  
                current = current.R
            elif current.L: 
                current = current.L
            else:  
                successor = current.R
                while successor.L:
                    successor = successor.L
                current.item = successor.item 
                current.R, _ = self.DeleteR(successor.item.ssn, current.R) 
        return current, deleted_item

    def Exists(self, ssn):
        return self.ExistsR(ssn, self.root)

    def ExistsR(self, ssn, current):
        if current is None:
            return False
        if ssn == current.item.ssn: 
            return True
        elif ssn < current.item.ssn:
            return self.ExistsR(ssn, current.L)
        else:
            return self.ExistsR(ssn, current.R)

    def Size(self):
        return self.SizeR(self.root)

    def SizeR(self, current):
        if current is None:
            return 0
        return 1 + self.SizeR(current.L) + self.SizeR(current.R)

    def __iter__(self):
        yield from self.IterR(self.root)

    def IterR(self, current):
        if current is not None:
            yield from self.IterR(current.L)
            yield current.item
            yield from self.IterR(current.R)

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
            person = bag.Retrieve(ssn)
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