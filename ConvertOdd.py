def transform_string(input_str):
    length = len(input_str)
    
    if length % 2 == 1:  # Check if the length of the string is odd
        middle = length // 2
        first_half = input_str[:middle].upper()
        second_half = input_str[middle:].lower()
        transformed_str = first_half + second_half
        return transformed_str
    else:
        return input_str.lower()

# Test cases
input_str1 = "oriJenBeliret"
input_str2 = "orionmeo"

transformed_str1 = transform_string(input_str1)
transformed_str2 = transform_string(input_str2)

print(f"Actual string: {input_str1} - Transformed string: {transformed_str1}")
print(f"Actual string: {input_str2} - Transformed string: {transformed_str2}")
