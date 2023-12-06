'''
The way that exception work is by attempting something
And then catching any error that occur during the attempt
'''

# Attempt, this will run in its entirity until it errors out (if it even does)
try:
    print("This is going to error" + 1)
# Catch, if the attempt fails, this block runs
except:
    print("This is the caught error")

'''
try

except

finally (optional) always runs regardless of everything else
'''

try:
    file = open("demo") # if this file doesnt exist
    # 1/0
    # pull some info from the file
    # make some changes
    # print some stuff out
    # DO THINGS
except FileNotFoundError:
    print("file does not exist")
    # print(1+1)
# You can have multiple except blocks
except Exception as e:
    print(e)
finally:
    print("This always prints")

def calculateSquareRoot(num):
    # # Error Checking
    # if type(num) is not int:
    #     raise Exception("This number must be an Integer")
    
    # if num < 0:
    #     raise Exception("This number must be positive")

    return num ** 0.5 # 4^1/2 = 2
    # Value of the function is the RETURN

# sqrt = calculateSquareRoot(2) # = 2
# print(sqrt)

try:
    # Casting - explicitly state what the type will be
    val = int(input("Enter a number here: "))
    result = calculateSquareRoot(val)
    print(f"This is the square root of {val}: {result}")
    val1 = int(input("Enter a number here: "))
    val2 = int(input("Enter a number here: "))
    result = val1 + val2
    print(f"This is the sum of {val1} and {val2}: {result}")


except Exception as e:
    print(e)
