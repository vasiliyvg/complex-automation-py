def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    # Initialize a variable to store the sum of digits
    digit_sum = 0

    # Iterate through each digit in the number string
    for digit_char in number_str:
        # Convert the digit character back to integer
        digit = int(digit_char)

        # Add the digit to the sum
        digit_sum += digit

    return digit_sum


# Example usage:
number = 3311211122211 # change this number to calculate
result = sum_of_digits(number)
print("Sum of digits in", number, "is:", result)