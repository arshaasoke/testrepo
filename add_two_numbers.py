def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    # Ask the user for input
    num1 = float(input("Enter first No: "))
    num2 = float(input("Enter second No: "))

    # Add the numbers
    result = add_two_numbers(num1, num2)

    # Display the result
    print("The sum is:", result)