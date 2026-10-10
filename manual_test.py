#!/usr/bin/env python3

import subprocess
import sys
import os

# Create a simple test by simulating input
def test_script_with_input(script_path, input_text):
    """Test script with specific input"""
    process = subprocess.Popen(
        [sys.executable, script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_text)
    return stdout.strip(), stderr.strip(), process.returncode

# Test cases
test_cases = [
    ("7\n", "7 is odd."),
    ("4\n", "4 is even."),
    ("0\n", "0 is even."),
    ("-5\n", "-5 is odd."),
    ("abc\n", "Please enter a valid integer."),
    ("3.14\n", "Please enter a valid integer.")
]

print("Testing even_odd.py script:")
print("=" * 40)

for input_val, expected in test_cases:
    stdout, stderr, returncode = test_script_with_input('even_odd.py', input_val)
    
    print(f"Input: {repr(input_val)}")
    print(f"Output: {repr(stdout)}")
    print(f"Expected: {repr(expected)}")
    
    if expected in stdout:
        print("✓ PASS")
    else:
        print("✗ FAIL")
    print("-" * 30)