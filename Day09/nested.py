capitals = {
    "Europe": "Berlin",
    "Asia": "Tokyo",
}

# Nested List in a Dictionary
countries = {
    "Europe": ["Germany", "France", "Italy"],
    "Asia": ["Japan", "China", "India"],
}

# print France
#print(countries["Europe"][1])

nested_list = ["A","B",["C","D"],"E"]
print(nested_list[2][1])  # Output: D

# Nested Dictionary
capitals = {
    "France": {
        "city": "Paris",
        "population": 2140526,
        "area": 105.4
    },
    "Germany": {
        "city": ["Berlin", "Munich","Hamburg"],
        "population": 83783942,
    },
}

# Print Hamburg
print(capitals["Germany"]["city"][2])  # Output: Hamburg
 