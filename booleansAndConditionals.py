""" 
A boolean is a data type that represent two possibilities:
    True - 1 - successful
    False - 0 - failure
    This is what your computer uses to do literally everything
    10101010111101011101010101011101010101010101110101010101011010
"""
iAmTrue = True
iAmFalse = False

print(iAmTrue)
print(iAmFalse)

# casting
print(bool(1))
print(bool(0))

'''
Boolean Operators (equations)
==          Equals                      5==5 - true
!=          Not Equals                  5!=5 - false
>           Greater than                5>4 - true
<           Less than                   5<4 - false
>=          Greater than or equal to    5>=5 - true
<=          Less than or equal to       5<=5 - true
'''

# 1 ='s is assignment
correct = True
incorrect = False

# 2 ='s is equating
print("Variable 1 and Variable 2 evaluate to: ", correct != incorrect)

print(13 > 7) # true
print(43 < 8) # False
print(8 <= 9) # true
print(8 >= 8) # True

"""  
and - when added to a boolean statement it allows you to add other statements to be evaluated
The add operator will check if BOTH statements are true before returning true.
"""
print(13 > 7 and 8 <= 9)

"""  
or - when added to a boolean statement it will check if one statment OR another statement is true
If even one of them is true, it will return true. Will only return false when both are false 
"""
print(13 > 13 or 8 <= 7)


# Conditional Statements (conditionals) (branching)
# Make decsion in our code
# Absolutely essential part of coding
# Allows us to create outputs based on True/False values and complete different activities as a result.
# Keywords: if, else, elif (else if)

sunshine = True
# If there is sunshine, lets go outside. Otherwise, lets stay inside.
if sunshine is not True: # If this
    print("Lets go outside") # Then that
else: # Otherwise
    print("Lets stay inside") # Do this

# is, ==
# is not, !=

# You can only have 1 if and 1 else, but as many elif's as you want

pokemon = "Pikachu"
if pokemon == "Pikachu": #False
    print("pika pika") # Execute
elif pokemon == "Gastly": # This line is only executed if above isnt true
    print("gastly")
else: # Catch all
    print("IDK bro")

# The elif statment will run only run if the above statement was false

# Down here

# consecutive if statements
""" 
You can "nest" if statements together to create webs of 
decision making
"""
pokeType = "ghost"
pokemonStr = "This is "
if pokemon == "Pikachu": # Both of these statements run
    pokemonStr += "Pikachu" # pokemonStr = pokemonStr + "Pikachu"
    if pokeType == "electric": # Both of these statements run
        pokemonStr += " they are an Electric type"
    if pokeType == "ghost": 
        pokemonStr += " they are an Ghost type"
        if True == True: 
            print("This is a triple nested statment")
print(pokemonStr)

