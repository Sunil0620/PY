
with open("Day26/Exercise_3/file1.txt", encoding="utf-8") as file:
    file_1 = [f.strip() for f in file]
with open("Day26/Exercise_3/file2.txt", encoding="utf-8") as file:
    file_2 = [f.strip() for f in file]
result = [int(num) for num in file_1 if num in file_2 ]

print(result)
