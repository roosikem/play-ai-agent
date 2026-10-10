#!/usr/bin/env python3

# Test script to verify reverse_text.py functionality

# Test 1: Normal text
test_input = "Hello World"
expected = "dlroW olleH"
result = test_input[::-1]
print(f"Test 1 - Normal text:")
print(f"Input: '{test_input}'")
print(f"Expected: '{expected}'")
print(f"Result: '{result}'")
print(f"Pass: {result == expected}\n")

# Test 2: Text with punctuation and spaces
test_input2 = "Hello, World!"
expected2 = "!dlroW ,olleH"
result2 = test_input2[::-1]
print(f"Test 2 - With punctuation:")
print(f"Input: '{test_input2}'")
print(f"Expected: '{expected2}'")
print(f"Result: '{result2}'")
print(f"Pass: {result2 == expected2}\n")

# Test 3: Empty string handling
test_input3 = ""
result3 = test_input3[::-1]
print(f"Test 3 - Empty input:")
print(f"Input: '{test_input3}'")
print(f"Result: '{result3}'")
print("Should print 'Please enter some text.' and exit")

# Test 4: Single character
test_input4 = "A"
expected4 = "A"
result4 = test_input4[::-1]
print(f"Test 4 - Single character:")
print(f"Input: '{test_input4}'")
print(f"Expected: '{expected4}'")
print(f"Result: '{result4}'")
print(f"Pass: {result4 == expected4}")