#!/usr/bin/env python3

# Test script for even_odd.py functionality
import subprocess
import sys

def test_even_odd():
    # Test cases
    test_cases = [
        ("7", "7 is odd."),
        ("4", "4 is even."),
        ("-3", "-3 is odd."),
        ("-2", "-2 is even."),
        ("0", "0 is even."),
        ("abc", "Please enter a valid integer."),
        ("", "Please enter a valid integer."),
        ("3.14", "Please enter a valid integer.")
    ]
    
    print("Testing even_odd.py script...")
    
    for input_val, expected in test_cases:
        # Write the input to a temporary file
        with open('test_input.txt', 'w') as f:
            f.write(input_val + '\n')
        
        # Run the script with the input
        try:
            result = subprocess.run([sys.executable, 'even_odd.py'], 
                                  stdin=open('test_input.txt', 'r'),
                                  capture_output=True, text=True, timeout=5)
            
            output = result.stdout.strip()
            print(f"Input: '{input_val}' -> Output: '{output}' (Expected: '{expected}')")
            
            if expected in output:
                print("✓ PASS")
            else:
                print("✗ FAIL")
            print()
        except Exception as e:
            print(f"Error testing input '{input_val}': {e}")
            print()

if __name__ == "__main__":
    test_even_odd()