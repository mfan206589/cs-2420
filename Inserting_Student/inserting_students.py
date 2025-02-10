import sys
import time
sys.setrecursionlimit(100000)
class Student:
    def __init__(self, SSN, email, last_name, first_name, age):
        self.fn = first_name
        self.ln = last_name
        self.SSN = SSN
        self.email = email
        self.age = age
    def __eq__(self, rhs):
        return self.SSN == rhs.SSN
class Bag:
    def __init__(self):
        self.item = []
    def insert(self, item):
        if item in self.item:
            return False
        else:
            self.item.append(item)
            return True
    def exist(self, item):
        if item in self.item:
            return True
        else:
            return False
    def size(self):
        return len(self.item)
def main():
    t1 = time.time()
    bag = Bag()
    with open('FakeNames.txt', 'r') as file:
        for line in file:
            data = line.strip().split()
            ln, fn, SSN, email, age = data
            student = Student(fn, ln, SSN, email, int(age))
            if not bag.insert(student):
                print(f'Duplicate Student Found: {fn}, {ln}')
    file.close()
    t2 = time.time()
    print(f"Total number of unique students. {bag.size()}")
    print(t2-t1)
main()