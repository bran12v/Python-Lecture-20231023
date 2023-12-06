# This is a comment in python, you can easily write comments or comment/uncomment items by using ctrl + /
# print("Hello World!")

# You can attach multiple strings together using the + sign
# print("This class is so much fun. I can't even believe how much I am learn right now" + 
#       "\nThis is on a new line" + " Another")

# print(1)

'''
This is a multiple line comment


Instead of writing a # before each line




I can just do this
'''
# Types in python
# Types are not required for declarations but they do still exist
'''
"string" - String
1 - integer
1.0 - float
true/false - boolean
['1', '2', '3'] - dynamic list
('1', '2', '3') - static list (tuple)
'''
# What do we use these types for?
# We use them for VARIABLES (Dynamic)
number = 3
# print(number)

# You can change variable, simply, by reassigning them
number = "String"
# print(number)

number = 4.0
# print(number)

'''
Operators (Math)
+           addition            4+4=8
-           subtraction         4-2=2
*           multiplication      4*2=8
/           division            4/2=2
%           modulus             17%3=2
**          exponent            4**2=16
//          floor division      9//2=4

Operators (equations)
==          Equals                      5==5 - true
!=          Not Equals                  5!=5 - false
>           Greater than                5>4 - true
<           Less than                   5<4 - false
>=          Greater than or equal to    5>=5 - true
<=          Less than or equal to       5<=5 - true
'''

num1 = 12
num2 = 7
# String and an integer
num3 = num1 + num2
# print(num3)
# String and an integer
# print("aasdadasdas" + num3)

# String and a String
# use the str() function to convert to string
# print("aasdadasdas" + str(19))

# What is a function?
# Some kind of action that takes an input and produces an output that is isolated from the rest of the program

# global scope
world = "world"

# declare functions in python "def"
def HelloWorld():
    # function scope
    hello = "hello "
    print(hello + world)
    # Code indent under a "def" is part of the function

# Code in a function does not run, UNLESS called
# HelloWorld()
# HelloWorld()
# HelloWorld()
# Function is ran when it is called! Not at definition
world = "Brandon"
# HelloWorld()
# HelloWorld()

# All code not indented under the "def" is not in the function
# print(world)

# hello world
# world

# Cant do this, variable is in function scope so the interpeter cant see it
# print(hello)

# Input parameters - You can provide a function with dynamic input values within the parenthesis
def Pokemon(sound, name, poketype):
    # functions HAVE to have code, you cant make an empty function

    # You can nest functions
    # by calling another function within a function
    HelloWorld()
    
    print(type(sound))
    print("Sound: ", sound)
    print(type(name))
    print("Name: ", name)
    print(type(poketype))
    print("Type: ", poketype)

Pokemon("Pika", "Pikachu", "Electric") # Functions reduce the amount of code we need to write to get the same results

Pokemon("Gen", "Gengar", "Ghost") # Allows for function to be dynamic in the results that they provide

Pokemon(1, 2, 3)

listexample = [1,2,3,4,5]
print(type(listexample))
