#!/usr/bin/env python3

def main():
    # Read input from user
    user_input = input("Enter text: ")
    
    # Check for empty input
    if not user_input:
        print("Please enter some text.")
        return
    
    # Reverse the text and print
    reversed_text = user_input[::-1]
    print(f"Reversed text: {reversed_text}")

if __name__ == "__main__":
    main()