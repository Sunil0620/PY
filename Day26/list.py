# List Comprehensions: Creating lists using a single line of code

numbers = [1, 2, 3, 4, 5]
new_list = [n * 2 for n in numbers]
# print(new_list)  # Output: [2, 4, 6, 8, 10]
name = "Sunil"
letter_list = [letter for letter in name]
range_list = [num * 2 for num in range(1,5)]

# Conditional List Comprehensions
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]
names = ["Sunil", "John", "Doe", "Jane"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
numbers = ['1', '2', '3', '4', '5']
# Convert strings to integers
int_numbers = [int(num) for num in numbers]
# print(int_numbers)  # Output: [1, 2, 3, 4, 5]

