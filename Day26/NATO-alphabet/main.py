import pandas as pd

#1.Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("Day26/NATO-alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for _, row in df.iterrows()}
# print(nato_dict)



#2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(output_list)
