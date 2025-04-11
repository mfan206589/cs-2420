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
        # Initialize a Student object with last name, first name, SSN, email, and age
        self.ln = ln
        self.fn = fn
        self.ssn = ssn
        self.email = email
        self.age = age

    def __hash__(self):
        # Define the hash function for a Student object based on their SSN
        return int(self.ssn.replace('-', ''))

    def __eq__(self, rhs):
        # Define equality for Student objects based on their SSN
        return self.ssn == rhs.ssn

# Define the Bag class to manage a collection of students
class Bag:
    def __init__(self, expandsize):
        # Initialize the hash table with a prime size larger than twice the expand size
        actualsize = expandsize * 2 + 1
        while not IsPrime(actualsize):
            actualsize += 2
        self.Table = [None] * actualsize

    def insert(self, item):
        # Insert a Student object into the hash table
        if self.exists(item):  # Check if the item already exists
            return False
        key = hash(item)  # Calculate the hash value of the item
        index = key % len(self.Table)  # Determine the starting index
        start_index = index  # Track the starting index to detect a full loop
        while self.Table[index] is not None:
            if self.Table[index] == item:
                return False  # Duplicate item
            index = (index + 1) % len(self.Table)  # Move to the next index
            if index == start_index:  # Full loop detected
                raise Exception("Hash table is full")
        self.Table[index] = item  # Insert the item into the hash table
        return True

    def exists(self, item):
        # Check if a Student object exists in the hash table
        key = hash(item)  # Calculate the hash value of the item
        index = key % len(self.Table)  # Determine the starting index
        start_index = index  # Track the starting index to detect a full loop

        while self.Table[index] is not None:
            if self.Table[index] == item:  # Check if the item matches
                return True
            index = (index + 1) % len(self.Table)  # Move to the next index
            if index == start_index:  # Full loop detected
                break
        return False  # Item not found

    def size(self):
        # Return the number of non-None items in the hash table
        return len([item for item in self.Table if item is not None])

    def delete(self, ssn):
        # Delete a Student object from the hash table based on their SSN
        key = int(ssn.replace('-', ''))  # Use the same logic as the Student __hash__ method
        index = key % len(self.Table)
        start_index = index  # Track the starting index to detect a full loop

        while self.Table[index] is not None:
            if self.Table[index].ssn == ssn:
                # Remove the item
                self.Table[index] = None

                # Shift subsequent elements to maintain the integrity of the hash table
                next_index = (index + 1) % len(self.Table)
                while self.Table[next_index] is not None:
                    rehash_item = self.Table[next_index]
                    self.Table[next_index] = None  # Remove the item temporarily

                    # Recalculate the correct position for the rehashed item
                    rehash_key = hash(rehash_item)
                    rehash_index = rehash_key % len(self.Table)
                    while self.Table[rehash_index] is not None:
                        rehash_index = (rehash_index + 1) % len(self.Table)

                    self.Table[rehash_index] = rehash_item  # Place the item in the correct position
                    next_index = (next_index + 1) % len(self.Table)

                return True
            index = (index + 1) % len(self.Table)
            if index == start_index:  # Full loop detected
                break
        return False  # Item not found

    def retrieve(self, ssn):
        # Retrieve a Student object from the hash table based on their SSN
        key = int(ssn.replace('-', ''))  # Use the same logic as the Student __hash__ method
        index = key % len(self.Table)
        while self.Table[index] is not None:
            if self.Table[index].ssn == ssn:
                return self.Table[index]  # Return the matching Student object
            index = (index + 1) % len(self.Table)  # Move to the next index
        return None  # Item not found

    def __iter__(self):
        # Allow iteration over non-None items in the hash table
        return (item for item in self.Table if item is not None)

def IsPrime(number):
    # Check if a number is prime
    if number < 2:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Main function to execute the program
def main():
    t1 = time.time()  # Start timing

    with open(Fake, 'r') as file:
        file_size = 0
        for line in file:
            file_size += 1
    bag = Bag(file_size)  # Create a new Bag instance
    TotalFails = 0
    # Insert students from FakeNames.txt
    with open(Fake, 'r') as file:
        for line in file:
            data = line.strip().split()  # Split the line into fields
            ln, fn, ssn, email, age = data
            student = Student(ln, fn, ssn, email, int(age))  # Create a Student object
            if not bag.insert(student):
                TotalFails += 1  # Increment the failure count if insertion fails

    t2 = time.time()  # Time after inserting students
    t3 = time.time()  # Start timing for retrieval

    # Retrieve students from RetrieveNames.txt and calculate average age
    with open(Retrieve, 'r') as file2:
        retrieved = []  # List to store retrieved SSNs
        total_age = 0
        total_people = 0
        for line in file2:
            retrieve_ssn = line.strip()  # Strip whitespace from the SSN
            retrieved.append(retrieve_ssn)
        for ssn in retrieved:
            person = bag.retrieve(ssn)  # Retrieve the Student object
            if person:
                total_age += person.age  # Add the age to the total
                total_people += 1  # Increment the count of retrieved people
            else:
                TotalFails += 1
        average = round(total_age / total_people, 5)  # Calculate average age

    t4 = time.time()  # Time after retrieval
    t5 = time.time()  # Start timing for deletion

    # Delete students from DeleteNames.txt
    with open(Delete, 'r') as file3:
        for line in file3:
            person = bag.delete(line.strip())  # Delete the Student object
            if person:
                pass
            else:
                TotalFails += 1

    t6 = time.time()  # Time after deletion

    # Print results
    print(f'Total Number of Fails: {TotalFails}')  # Print the total number of failures
    print(f'Total Number of Students: {bag.size()}')  # Print the number of remaining students
    print(f'Time Took to Total: {t2 - t1}')  # Print the time taken for insertion
    print(f'Average Age of Retrieved Students: {average}')  # Print the average age
    print(f'Time Took to Average: {t4 - t3}')  # Print the time taken for retrieval
    print(f'Time Took to Delete Students: {t6 - t5}')  # Print the time taken for deletion

# Run the main function
main()