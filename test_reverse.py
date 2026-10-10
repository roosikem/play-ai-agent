#!/usr/bin/env python3

def test_reverse_text():
    # Test normal text
    test_input = "Hello World"
    expected = "dlroW olleH"
    
    result = test_input[::-1]
    print(f"Input: '{test_input}'")
    print(f"Expected: '{expected}'")
    print(f"Result: '{result}'")
    print(f"Match: {result == expected}")
    
    # Test with punctuation and spaces
    test_input2 = "Hello, World!"
    expected2 = "!dlroW ,olleH"
    
    result2 = test_input2[::-1]
    print(f"\nInput: '{test_input2}'")
    print(f"Expected: '{expected2}'")
    print(f"Result: '{result2}'")
    print(f"Match: {result2 == expected2}")
    
    # Test empty input
    test_input3 = ""
    result3 = test_input3[::-1]
    print(f"\nInput: '{test_input3}'")
    print(f"Result: '{result3}'")
    print("Empty input test completed")

if __name__ == "__main__":
    test_reverse_text()