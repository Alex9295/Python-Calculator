# Define a function to display the calculator menu
def calculatorDisplay():
    # Create a multi-line string with the calculator options
    display = """Welcome to Calculator
    
Choose one operation:
1. Add
2. Subtract
3. Exit
"""
    return(display)  # Return the display string


# Define the main calculator function that performs operations based on user choice
def calculatorFunction(user_choice):
    # If user chooses addition (option 1)
    if user_choice == 1:
        print("Let's perform addition")
        # Get two numbers from user
        a, b = user_input()
        # Perform addition
        output = addition(a, b)
        # Return the result string
        return f"The sum is: {output}"
    # If user chooses subtraction (option 2)
    elif user_choice == 2:
        print("Let's perform subtraction")
        # Get two numbers from user
        a, b = user_input()
        # Perform subtraction
        output = subtraction(a, b)
        # Return the result string
        return f"The difference is: {output}"
    # If user chooses to exit (option 3)
    else:
        return("Exiting the calculator, bye bye!")

# Function to get user input for two numbers
def user_input():
    print("Give two numbers on two lines")
    # Get first number and convert to integer
    a = int(input("Number 1 is: "))
    # Get second number and convert to integer
    b = int(input("Number 2 is: "))
    # Return both numbers as a tuple
    return a, b

# Function to perform addition
def addition(a, b):
    return(a + b)  # Return the sum of a and b

# Function to perform subtraction
def subtraction(a, b):
    return(a - b)  # Return the difference between a and b


# Main program execution starts here
if __name__ == '__main__':
    # Create an infinite loop for the calculator
    while True:
        # Display the calculator menu
        print(calculatorDisplay())
        # Get user's choice of operation
        user_choice = int(input("Select the operation: "))
        # Perform the chosen operation and get result
        value = calculatorFunction(user_choice)
        # Print the result
        print(value)
        # If user chose to exit, break the loop to end the program
        if value == "Exiting the calculator, bye bye!":
            break
