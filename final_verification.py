#!/usr/bin/env python3

# Final verification that even_odd.py meets all requirements

import os

def check_script():
    # Check if file exists
    if not os.path.exists('even_odd.py'):
        print("ERROR: even_odd.py file not found")
        return False
    
    # Read the script
    with open('even_odd.py', 'r') as f:
        content = f.read()
    
    print("Script content:")
    print(content)
    print("=" * 50)
    
    # Verify requirements
    requirements = [
        ("Uses input() function", "input(" in content),
        ("Handles integer conversion", "int(" in content),
        ("Checks even/odd with modulo", "% 2" in content or "mod" in content),
        ("Handles ValueError exception", "ValueError" in content),
        ("Prints 'Please enter a valid integer.'" , "Please enter a valid integer." in content),
        ("Uses only standard library", "import" not in content or "import sys" in content or "import os" in content),  # Basic check
    ]
    
    print("Requirements verification:")
    all_good = True
    for req, met in requirements:
        status = "✓" if met else "✗"
        print(f"{status} {req}")
        if not met:
            all_good = False
    
    print("\n" + "=" * 50)
    if all_good:
        print("✓ All requirements satisfied!")
    else:
        print("✗ Some requirements not met")
    
    return all_good

if __name__ == "__main__":
    check_script()