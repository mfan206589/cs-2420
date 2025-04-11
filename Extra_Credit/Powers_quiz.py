import random
import time

def main():
    # Generate all powers of 2 from 0 to 49
    powers = {i: 2 ** i for i in range(50)}
    
    # Get the list of exponents and shuffle them
    exponents = list(powers.keys())
    random.shuffle(exponents)
    
    # Start the timer
    start_time = time.time()
    
    # Quiz the user
    for exponent in exponents:
        correct_answer = powers[exponent]
        while True:
            try:
                user = int(input(f"What is 2 ** {exponent} ? "))
                if user == correct_answer:
                    break
                else:
                    print("Wrong! Try again:", end=" ")
            except ValueError:
                print("Please enter a valid integer.")
    
    # Calculate the total time taken
    total_time = time.time() - start_time
    print(f"Your total time was {int(total_time)} seconds.")

if __name__ == "__main__":
    main()