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

# Define the Bag class to manage a collection of students
class Bag:
    def __init__(self):
        self.people = []

    def insert(self, item):
        if self.exists(item):
            return False
        else:
            self.people.append(item)
            return True

    def exists(self, item):
        if item in self.people:
            return True
        else:
            return False

    def size(self):
        return len(self.people)

    def delete(self, ssn):
        person = self.retrieve(ssn)
        if person:
            self.people.remove(person)
            return True

    def retrieve(self, ssn):
        for person in self.people:
            if person.ssn == ssn:
                return person

    def __iter__(self):
        return iter(self.people)

# Main function to execute the program
def main():
    t1 = time.time()  # Start timing
    bag = Bag()  # Create a new Bag instance

    # Insert students from FakeNames.txt
    with open(Fake, 'r') as file:
        for line in file:
            data = line.strip().split()
            ln, fn, ssn, email, age = data
            student = Student(ln, fn, ssn, email, int(age))
            if not bag.insert(student):
                print(f"Duplicate Student: {ssn}")

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
            person = bag.retrieve(ssn)
            if person:
                total_age += person.age
                total_people += 1
            else:
                print(f'Unable to Retrieve: {ssn}')
        average = round(total_age / total_people, 5)  # Calculate average age

    t4 = time.time()  # Time after retrieval
    t5 = time.time()  # Start timing for deletion

    # Delete students from DeleteNames.txt
    with open(Delete, 'r') as file3:
        for line in file3:
            person = bag.delete(line.strip())
            if person:
                pass
            else:
                print(f'Unable to Delete: {line}')

    t6 = time.time()  # Time after deletion

    # Print results
    print(f'Total Number of Students: {bag.size()}')
    print(f'Time Took to Total: {t2 - t1}')
    print(f'Average Age of Retrieved Students: {average}')
    print(f'Time Took to Average: {t4 - t3}')
    print(f'Time Took to Delete Students: {t6 - t5}')

# Run the main function
main()