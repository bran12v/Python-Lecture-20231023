"""
alt-shift-a - multi line comment
ctrl-/ - comment
tab - indent
shift-tab - revert intent
ctrl-z - redo
ctrl-c - copy
ctrl-v - paste
ctrl-shift-p - search word wrap or alt-z
ctrl-arrowkey - jump words - add shift to highlight
windows-shift-s
"""

# Dictionaries
# Key-value data structure in python (DynamoDB)
dictionary1 = {"one": 1, "two": 2, "three": 3} # This looks just like JSON
# print(dictionary1)

# Print a specific item in the dictionary
# print(dictionary1["three"])

# You can pull values from a dictionary by looking up their key
# However!!! You cannot do it the other way around (One-way)
# print(dictionary1[3]) # This will not work

dictionary2 = {
    "Pikachu": "Electric",
    "Zapdos": "Electric",
    "Squirtle": "Water",
    "Mewoth": 1
}
# print(dictionary2)
emptydict = {}
# print(emptydict)

# Add to a dictionary
example1 = {}
# Key does not currently exist, python will make a new entry with the key and value in the dictionary
example1["Brandon"] = "has a strong name"
# print(example1)
# I can change already created keys in the same way
example1["Brandon"] = 1
# print(example1)
# Keys are unique, immutable - we dont expect change
example1["Mason"] = "hombre"
# print(example1)

# This is another way to add to a dictionary
# This way allows you to add multiple values at once
# Casing is IMPORTANT (Case sensitive)
example1.update({"Will": "Plaid", "Rommel": "Jacket", "mason": 1})
# print(example1)

# This is how you can delete from a dictionary
# del example1["mason"]
example1.pop("mason")
# print(example1)

# You can put a dictionary inside of a dictionary if you need to provide more context about the items in your dictionary
nestedDictionary = {
    "Pikachu": "Electric",
    "Zapdos": "Electric",
    "Squirtle": "Water",
    "Meowth": {
        "type": "Normal",
        "demeanor": "mean",
        "Money": "none"
    }
}

print(nestedDictionary["Meowth"]["type"])

# Example 
# Item is going to be a key, rather than a value
for item in nestedDictionary:
    # print(item)
    if nestedDictionary[item] is dict:
        for i in item:
            print(f"This is an example of print items in a nested loop: {i}")
            #in the second for loop
        #in the if statement
    #in the first for loop
    else:
        print(f"This is an example of print items in a nested loop: {nestedDictionary[item]}")

# If i add .values() to my dictionary it iterates over the values instead
print(nestedDictionary.values())
for item in nestedDictionary.values():
    # print(item)
    if item is dict:
        for i in item:
            print(f"This is an example of print items in a nested loop: {i}")
            #in the second for loop
        #in the if statement
    #in the first for loop
    else:
        print(f"This is an example of print items in a nested loop: {item}")

# ------------------------------------------------------------------------------------------
