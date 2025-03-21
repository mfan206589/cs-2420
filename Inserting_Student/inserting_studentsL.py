import time
from pathlib import Path
root_dir = Path(__file__).parent
Fake = root_dir / 'FakeNames.txt'
Retrieve = root_dir / 'RetrieveNames.txt'
Delete = root_dir / 'DeleteNames.txt'
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
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt
class Bag:
    def __init__(self):
        self.first = None
    def Insert(self, item):
        if self.Exists(item):
            return False
        else:
            n = Node(item, self.first)
            self.first = n
            return True
###This is the advance method for checking the full linked lists
    #While current:
        #current = current.nxt
###
    def Exists(self, item):
        return item in self
    def Size(self):
        size = 0
        current = self.first
        while current:
            size += 1
            current = current.nxt
        return size
    def Retrieve(self, ssn):
        current = self.first
        while current:
            if current.item.ssn == ssn:
                return current.item
            current = current.nxt
        return None
    def Delete(self, ssn):
        current = self.first
        previous = None
        while current:
            if current.item.ssn == ssn:  # Compare the SSN directly
                if previous is None:  # Deleting the first node
                    self.first = current.nxt
                else:  # Deleting a node in the middle or end
                    previous.nxt = current.nxt
                return current.item  # Return the deleted Student object
            previous = current
            current = current.nxt
        return None
    def __iter__(self):
        current = self.first
        while current:
            yield current.item
            current = current.nxt
def main():
    bag = Bag()
    t1 = time.time()
    with open(Fake, 'r') as file:
        for line in file:
            data = line.strip().split()
            ln, fn, ssn, email, age = data
            student = Student(ln, fn, ssn, email, int(age))
            if not bag.Insert(student):
                print(f"Duplicate Student: {ssn}")
    t2 = time.time()
    t3 = time.time()
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
                print(f'Unable to Retrieve: {ssn}')
        average = round(total_age/total_people, 5)
    t4 = time.time()
    t5 = time.time()
    with open(Delete, 'r') as file3:
        for line in file3:
            person = bag.Delete(line.strip())
            if person:
                pass
            else:
                print(f'Unable to Delete: {line}')
    t6 = time.time()
    print(f'Total Number of Students: {bag.Size()}')
    print(f'Time Took to Total: {t2-t1}')
    print(f'Average Age of Retrived Students: {average}')
    print(f'Time Took to Average: {t4-t3}')
    print(f'Time Took to Delete Students: {t6 - t5}')
main()