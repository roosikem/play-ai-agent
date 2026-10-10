#!/usr/bin/env python3

# Prompt user for input
user_input = input("Enter an integer: ")

try:
    # Try to convert input to integer
    number = int(user_input)
    
    # Check if even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
        
except ValueError:
    # Handle invalid input
    print("Please enter a valid integer.")