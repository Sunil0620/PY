# Divison -> 5/2 = 2.5    (default in Python 3)
# Double Slash -> 5//2 = 2  (floor division)
# Integer Division -> 5//2 = 2
# Modulus -> 5%2 = 1  (remainder)
# Exponentiation -> 5**2 = 25

# Max/Min Int
float('inf')
float('-inf')

# Py Numbers are infinite so they never **OVERFLOW**
import math      
print(math.pow(2, 300))

#But still less than infinity
print(math.pow(2, 300) < float('inf'))  # True

# List Comprehensions
arr = [1,2,3,4,5]
print(arr)
# Can be used as a stack
arr.append(6)  # Push
print(arr)     # [1, 2, 3, 4, 5, 6]

arr.pop()     # Pop 
print(arr)    # [1, 2, 3, 4, 5]
arr.insert(0, 0)  # Insert at the beginning or in middle
print(arr)    # [0, 1, 2, 3, 4, 5]

# Careful: _1 is not out of bounds, its last value
print(arr[-1])   # 5

# Sublists (Slicing)
print(arr[1:3])  # [2, 3] (from index 1 to 2)

# Unpacking
a, b, c = [1, 2, 3]
# Loops through arr
for i in range(len(arr)):
    print(arr[i])  # Prints each element in arr
# Enumerate
for index, value in enumerate(arr):
    print(f"Index: {index}, Value: {value}")  # Prints index and value

# Zip -> Pairs elements from multiple lists OR Arrays
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for l1, l2 in zip(list1, list2): 
    print(l1, l2)  # Prints pairs (1, 'a'), (2, 'b'), (3, 'c')

# Reverse()
arr.reverse()  # In-place reverse
print(arr)  # [5, 4, 3, 2, 1, 0]
# Sort()
arr.sort()  # In-place sort
print(arr)  # [0, 1, 2, 3, 4, 5]
arr.sort(reverse=True)  # Sort in descending order
# List Comprehensions
arr = [i+i for i in range(4)]
print(arr)  # [0, 2, 4, 6]
# String are similar to lists but immutable canot be changed
# ASCII Values -> ord()
print(ord('A'))  # 65
#delimiter = ' 'or ""  combine strings
strings = ["a", "b", "c"]
print("".join(strings))  # 'abc'

# Queues (double ended queues) implementation
from collections import deque

queue = deque()
queue.append(1) # Add to the right
queue.append(2) 
print(queue)  # deque([1, 2])
# Added: Demonstrate left-side operations
queue.appendleft(0)  # Add to the left
print(queue)  # Expected: deque([0, 1, 2])
queue.popleft()  # Remove from the left
print(queue)  # Expected: deque([1, 2])
# set comprehensions
set_example = {x for x in range(5) if x % 2 == 0}
print(set_example)  # {0, 2, 4}
# Dictionary comprehensions HashMap
myMap = {x: x**2 for x in range(5)}
