def clean_string_with_datastructures(input_string):
    result_string = ""

    for char in input_string:
        if char.isalpha() or char.isspace():
            result_string += char
        elif char.isdigit():
            result_string += ''
        else:
            result_string += ' '

    return result_string

# Example usage:
input_string = "Hello123 This is a 1495 sample string with $pecial#$ characters."
cleaned_string = clean_string_with_datastructures(input_string)

print(f"Original String: {input_string}")
print(f"Cleaned String: {cleaned_string}")

# Write a program to remove all numbers and replaces all special characters with a space
# from a string
