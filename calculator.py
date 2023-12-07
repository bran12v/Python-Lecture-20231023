"""  
1. Create a function that takes two parameters and returns their sum.
2. Create a function that takes two parameters and returns their difference.
3. Create a function that takes two parameters and returns them multiplied.
4. Create a function that takes two parameters and returns them divided.
5. Create tests in your main function showing the results of each function printed out to the 
command line.
6. Submit a screenshot of the results in the console.
"""
# Sum
def sum(x, y):
    try:
        return int(x) + int(y) # if this action cannot be completed then
    except:
        return "Unsupported operation" # This message will be returned
 
# difference
def difference(x, y):
    try:
        return int(x) - int(y)
    except:
        return "Unsupported operation"

# multiplication
def multiply(x, y):
    try:
        return int(x) * int(y)
    except:
        return "Unsupported operation"
    
# division
def divide(x, y):
    try:
        return int(x) / int(y)
    except:
        return "Unsupported operation"

# The main function is the entry point for your program
def main():
    while True:
        mathSymbol = input("Enter symbol here: ") # +, -, *, /
        # 5 + 5
        if mathSymbol == "+":
            x = input("Enter number for addition: ")
            y = input("Enter number for addition: ")
            print(f"This is the sum of {x} and {y}: {sum(x,y)}")
        #-
        elif mathSymbol == "-":
            x = input("Enter number for subtraction: ")
            y = input("Enter number for subtraction: ")
            print(f"This is the difference of {x} and {y}: {difference(x,y)}")
        #*
        elif mathSymbol == "*":
            x = input("Enter number for multiplication: ")
            y = input("Enter number for multiplication: ")
            print(f"This is the multiplication of {x} and {y}: {multiply(x,y)}")
        #/
        elif mathSymbol == "/":
            x = input("Enter number for division: ")
            y = input("Enter number for division: ")
            print(f"This is the division of {x} and {y}: {divide(x,y)}")
        else: # Catch all
            print("Not a valid symbol")

        # Advanced version
        # equation = input("Enter equation here: ")
        # values = equation.split(" ")
        # if values[1] == "+":
        #     print(int(values[0]) + int(values[2]))

if __name__ == "__main__":
    main()