import time
from pathlib import Path

# Define file paths
root_dir = Path(__file__).parent
Fake = root_dir / 'FakeNamesM.txt'
Retrieve = root_dir / 'RetrieveNamesM.txt'
Delete = root_dir / 'DeleteNamesM.txt'

# Define the Student class
class Student:
    def __init__(self, ln, fn, ssn, email, age):
        # Initialize a Student object with last name, first name, SSN, email, and age
        self.ln = ln
        self.fn = fn
        self.ssn = ssn
        self.email = email
        self.age = age

    def __eq__(self, rhs):
        # Define equality for Student objects based on their SSN
        return self.ssn == rhs.ssn

# Define the Node class for the binary search tree
class Node:
    def __init__(self, item):
        # Initialize a Node with a Student object and left/right child pointers
        self.item = item
        self.L = None
        self.R = None

# Define the Bag class to manage a collection of students using a binary search tree
class Bag:
    def __init__(self):
        # Initialize the Bag with an empty root
        self.root = None

    def Insert(self, item):
        # Insert a Student object into the binary search tree
        if self.Exists(item.ssn):  # Check if the student already exists
            return False
        self.root = self.InsertR(item, self.root)  # Recursively insert the student
        return True

    def InsertR(self, item, current):
        # Recursive helper function to insert a Student into the tree
        if current is None:
            current = Node(item)  # Create a new node if the current position is empty
        elif item.ssn < current.item.ssn:
            current.L = self.InsertR(item, current.L)  # Insert into the left subtree
        else:
            current.R = self.InsertR(item, current.R)  # Insert into the right subtree
        return current

    def Retrieve(self, ssn):
        # Retrieve a Student object from the binary search tree based on their SSN
        return self.RetrieveR(ssn, self.root)

    def RetrieveR(self, ssn, current):
        # Recursive helper function to retrieve a Student from the tree
        if current is None:
            return None  # Return None if the student is not found
        if ssn == current.item.ssn:
            return current.item  # Return the matching Student object
        elif ssn < current.item.ssn:
            return self.RetrieveR(ssn, current.L)  # Search in the left subtree
        else:
            return self.RetrieveR(ssn, current.R)  # Search in the right subtree

    def Delete(self, ssn):
        # Delete a Student object from the binary search tree based on their SSN
        if not self.Exists(ssn):  # Check if the student exists
            return None
        self.root, deleted_item = self.DeleteR(ssn, self.root)  # Recursively delete the student
        return deleted_item

    def DeleteR(self, ssn, current):
        # Recursive helper function to delete a Student from the tree
        if current is None:
            return current, None
        if ssn < current.item.ssn:
            current.L, deleted_item = self.DeleteR(ssn, current.L)  # Delete from the left subtree
        elif ssn > current.item.ssn:
            current.R, deleted_item = self.DeleteR(ssn, current.R)  # Delete from the right subtree
        else:
            deleted_item = current.item  # Found the node to delete
            if current.L is None:  # Node with only right child or no child
                return current.R, deleted_item
            elif current.R is None:  # Node with only left child
                return current.L, deleted_item
            # Node with two children: Get the inorder successor
            successor = self.GetMinValueNode(current.R)
            current.item = successor.item  # Replace with the successor
            current.R, _ = self.DeleteR(successor.item.ssn, current.R)  # Delete the successor
        return current, deleted_item

    def GetMinValueNode(self, current):
        # Find the node with the smallest value in the subtree
        while current.L is not None:
            current = current.L
        return current

    def Exists(self, ssn):
        # Check if a Student object exists in the binary search tree based on their SSN
        return self.ExistsR(ssn, self.root)

    def ExistsR(self, ssn, current):
        # Recursive helper function to check if a Student exists in the tree
        if current is None:
            return False
        if ssn == current.item.ssn:
            return True
        elif ssn < current.item.ssn:
            return self.ExistsR(ssn, current.L)  # Search in the left subtree
        else:
            return self.ExistsR(ssn, current.R)  # Search in the right subtree

    def Size(self):
        # Return the total number of students in the binary search tree
        return self.SizeR(self.root)

    def SizeR(self, current):
        # Recursive helper function to calculate the size of the tree
        if current is None:
            return 0
        return 1 + self.SizeR(current.L) + self.SizeR(current.R)

    def __iter__(self):
        # Allow iteration over the students in the binary search tree (in-order traversal)
        yield from self.IterR(self.root)

    def IterR(self, current):
        # Recursive helper function for in-order traversal
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
            data = line.strip().split()  # Split the line into fields
            ln, fn, ssn, email, age = data
            student = Student(ln, fn, ssn, email, int(age))  # Create a Student object
            if not bag.Insert(student):  # Insert the student into the tree
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
            person = bag.Retrieve(ssn)  # Retrieve the Student object
            if person:
                total_age += person.age  # Add the age to the total
                total_people += 1  # Increment the count of retrieved people
            else:
                TotalFails += 1  # Increment the failure count if retrieval fails
        average = round(total_age / total_people, 5)  # Calculate average age

    t4 = time.time()  # Time after retrieval
    t5 = time.time()  # Start timing for deletion

    # Delete students from DeleteNames.txt
    with open(Delete, 'r') as file3:
        for line in file3:
            person = bag.Delete(line.strip())  # Delete the Student object
            if person:
                pass
            else:
                TotalFails += 1  # Increment the failure count if deletion fails

    t6 = time.time()  # Time after deletion

    # Print results
    print(f'Total Number of Fails: {TotalFails}')  # Print the total number of failures
    print(f'Total Number of Students: {bag.Size()}')  # Print the number of remaining students
    print(f'Time Took to Total: {t2 - t1}')  # Print the time taken for insertion
    print(f'Average Age of Retrieved Students: {average}')  # Print the average age
    print(f'Time Took to Average: {t4 - t3}')  # Print the time taken for retrieval
    print(f'Time Took to Delete Students: {t6 - t5}')  # Print the time taken for deletion

# Run the main function
main()