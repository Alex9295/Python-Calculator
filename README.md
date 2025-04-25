Overview
This is a simple command-line calculator program written in Python that performs basic arithmetic operations. The program allows users to choose between addition and subtraction, 
or exit the calculator.

Features
Addition of two numbers

Subtraction of two numbers

Interactive command-line interface

Clear operation selection menu

Proper input validation (expects integers)

How to Use
Run the program in a Python environment (Python 3.x recommended)

You'll see a welcome message with operation options:

1. Add
2. Subtract
3. Exit
Enter your choice (1, 2, or 3)

For addition or subtraction:

The program will prompt you to enter two numbers

It will then display the result

The program will continue running until you choose option 3 to exit

Functions
calculatorDisplay(): Displays the welcome message and operation options

calculatorFunction(user_choice): Handles the operation based on user input

user_input(): Collects two numbers from the user

addition(a, b): Performs addition of two numbers

subtraction(a, b): Performs subtraction of two numbers

Requirements
Python 3.x

Running the Program
Simply execute the Python script in your terminal or IDE:

bash
python calculator.py
Example Usage
Welcome to Calculator

Choose one operation:
1. Add
2. Subtract
3. Exit

Select the operation: 1
Let's perform addition
Give two numbers on two lines
Number 1 is: 5
Number 2 is: 3
The sum is: 8
Exit the Program
To exit, select option 3 when prompted for operation selection. The program will display "Exiting the calculator, bye bye!" and terminate.
