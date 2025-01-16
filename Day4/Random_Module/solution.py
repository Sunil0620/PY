#lists : Create a list of numbers:

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
my_list[1] = 10
print(my_list)  # Output: [1, 10, 3, 4, 5]
 
# Add an element to the end of the list: append() method or insert() method:

my_list.append(6)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]
my_list.insert(1, 15)
print(my_list)  # Output: [1, 15, 10, 3, 4, 5, 6]

# Remove an element from the list: remove() method or pop() method or del statement:

my_list.remove(10)
print(my_list)  # Output: [1, 15, 3, 4, 5, 6]
my_list.pop(1)
print(my_list)  # Output: [1, 3, 4, 5, 6]
del my_list[0]
print(my_list)  # Output: [3, 4, 5, 6]

#Iterate over a list using for loop:
for item in my_list:
    print(item)

# Concatenate two lists: + operator or extend() method:
# Method 1: Using + operator:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Method 2: Using extend() method:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

#Nested lists:
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "spinach", "broccoli"]
grocery_list = [fruits, vegetables]
print(grocery_list)
