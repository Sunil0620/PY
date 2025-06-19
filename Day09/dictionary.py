programing_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected.",
    "function": "A block of code that only runs when it is called.",
}

print(programing_dictionary["bug"])
# Add new key-value pairs to the dictionary
programing_dictionary["loop"] = "The action of doing something over and over again."
print(programing_dictionary["loop"])

programing_dictionary["bug"] = "A mistake in a program that causes it to behave unexpectedly."
print(programing_dictionary["bug"])
empty_dictionary = {}
#Wipe an existing dictionary
#programing_dictionary = {}
#print(programing_dictionary)

# loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])
