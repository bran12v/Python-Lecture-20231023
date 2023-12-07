# Loops are blocks that allow us to run code multiple times
# Based on conditions that we set.
# There are two types of loops that we will talk about:
# While loops, for loops

"""  
A while loop 

Execute code indented inside of it while a certian condition is met.
Once the condition is not met, then the loop will terminate.

It will execute code WHILE a condition is true UNTIL the condition is false
"""

num = 3

# while num > 0: # infinite loop, loop never ends
#     print(num)
#     num -= 1 # num = num - 1

names = ["Nathanael", "Brianna", "Brandon", "Mayito", "Rommel", "William", "Joshua", "Sergio", "Isaiah", "Mason", "Kendall", "Kevin", "Elton"]

# while num >= 0:
#     print(f"This is {names[num]}")
#     num -= 1

"""  
The For loop

It executes the lines of code indented inside of it for a set number of times

Structure of a for loop:
for [variable name] in [number of times] 
    range(1,6)
    list

    Addition loop keywords:
        Break - stops the CURRENT loop
        Continue - moves the loop immediately to the next iteration
        Pass (not commonly used) - placeholder

"""
# Lists in python start at 0
# range(0,13) 0-12
for i in range(0,13):
    print(i)
    pass # Do nothing
    # The i variable changes every time the loop iterates. It will become the next value
    if names[i] == "Brandon":
        continue
    print(names[i])
    while num > 0: # Nested loop
        print("\tHahaha\n")
        num -= 1
        break
    num = 3