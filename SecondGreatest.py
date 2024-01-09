# def find_second_and_fourth_greatest(numbers):
#     if len(numbers) < 4:
#         return "Error: List has less than 4 numbers."

#     # Sort the list in descending order
#     sorted_numbers = sorted(numbers, reverse=True)

#     # Find the second and fourth greatest numbers
#     second_greatest = sorted_numbers[1]
#     fourth_greatest = sorted_numbers[3]

#     return second_greatest, fourth_greatest

# # Example usage:
# numbers_list = [10, 5, 8, 20, 15, 7]
# result = find_second_and_fourth_greatest(numbers_list)

# if isinstance(result, tuple):
#     second_greatest, fourth_greatest = result
#     print(f"Second greatest number: {second_greatest}")
#     print(f"Fourth greatest number: {fourth_greatest}")
# else:
#     print(result)

def find_second_and_fourth_greatest(numbers):
    if len(numbers) < 4:
        return "Error: List has less than 4 numbers."

    first, second, third, fourth = float('-inf'), float('-inf'), float('-inf'), float('-inf')

    for num in numbers:
        if num > first:
            first, second, third, fourth = num, first, second, third
        elif num > second:
            second, third, fourth = num, second, third
        elif num > third:
            third, fourth = num, third
        elif num > fourth:
            fourth = num

    return second, fourth

# Example usage:
numbers_list = [10, 5, 8, 20, 15, 7]
result = find_second_and_fourth_greatest(numbers_list)

if isinstance(result, tuple):
    second_greatest, fourth_greatest = result
    print(f"Second greatest number: {second_greatest}")
    print(f"Fourth greatest number: {fourth_greatest}")
else:
    print(result)

