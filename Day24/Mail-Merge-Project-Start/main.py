PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", encoding="utf-8") as name_files:
    names = name_files.readlines()
    
with open("Input/Letters/starting_letter.txt", encoding="utf-8") as letter_files:
    content_file = letter_files.read()
    for name in names:
        stripped_name = name.strip()
        replace = content_file.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docx", "w", encoding="utf-8") as letters:
            letters.write(replace)
           