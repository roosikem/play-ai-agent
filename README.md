# Play AI Agent

This is a Play Framework application with a Hello World example.

## Running the Application

To run the application, use:

```
sbt run
```

Then visit `http://localhost:9000` to see the home page, or `http://localhost:9000/hello` to see the Hello World message.

## even_odd.py

A Python script that determines whether a user-provided integer is even or odd.

### Features
- Prompts user with "Enter an integer:"
- Handles positive integers (e.g., 7 → "7 is odd.")
- Handles negative integers (e.g., -4 → "-4 is even.")
- Identifies zero as even (0 → "0 is even.")
- Provides clear error handling for invalid input
- Uses only Python's standard library

### Usage
```bash
python3 even_odd.py
```

### Example outputs
```
Enter an integer: 7
7 is odd.

Enter an integer: -4
-4 is even.

Enter an integer: 0
0 is even.

Enter an integer: abc
Please enter a valid integer.
```