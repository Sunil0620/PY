# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for(key, value) in dict.items() if test}

import random

names = {'Sunil', 'Beth', 'Alex', 'Dave', 'Caroline', 'Freddie'}
scores = {student:random.randint(1, 100) for student in names}
passed = {student:score for (student, score) in scores.items() if score >= 60}
# print(passed)

example_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
new_dict = {key: value ** 2 for (key, value) in example_dict.items() if value % 2 == 0}
# print(new_dict)
sentence = "This is an example sentence."
words = sentence.split()
result = {word: len(word) for word in words}
print(result)