#Here is the list of student scores. Your task is to find the highest score from the list.
scores = [78, 85, 95, 62, 88, 90, 99, 73]

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")
