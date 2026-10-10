#!/usr/bin/env python3

"""
A Python script that prompts the user for two numbers and prints their sum.
Handles invalid input gracefully.
"""

def main():
    try:
        # Get first number from user
        first_number = input("Enter first number: ")
        num1 = float(first_number)
        
        # Get second number from user
        second_number = input("Enter second number: ")
        num2 = float(second_number)
        
        # Calculate and print the sum
        result = num1 + num2
        print(f"Sum: {result}")
        
    except ValueError:
        # Handle invalid input
        print("Please enter valid numbers.")
        return

if __name__ == "__main__":
    main()