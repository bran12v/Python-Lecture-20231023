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


try:
    file = open("demo") # if this file doesnt exist
    # pull some info from the file
    # make some changes
    # print some stuff out
    # DO THINGS
except:
    print("file does not exist")
    # print(1+1)

