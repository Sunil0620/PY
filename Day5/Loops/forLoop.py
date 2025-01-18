# for loop with range() function:
for i in range(5):
    print(i)

# nested for loop:  
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}\n")

# break: Exits the loop prematurely.
# continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

for i in range(10):
    if i == 5:
        break
    print(i)      # Output: 0 1 2 3 4


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)      # Output: 1 3 5 7 9

