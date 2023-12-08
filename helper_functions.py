"""
Small, modularized, neat, code that we can use/reuse for common actions
Divide and conquer
"""
# from - this the package that the code comes from
# import - keyword that allows you to grab code from other peoples libraries and run it in your program
from datetime import datetime
import random

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# that gets the current time
def get_current_time():
    return datetime.now().time()

# Get date
def get_current_date():
    return datetime.now().date()

# Formats that time into something nice
def format_date(date, time):
    return f"{date}, {time}"

def rand_int():
    return random.randint(1,10)

def main():
    # command to open file
    write_file("test.txt", "Hello")
    print(read_file("test.txt"))
    print(format_date(get_current_date(), get_current_time()))
    list1 = [1,2,3,3,4,55,5,6,2,3]
    for i in range(0,2):
        print(list1[rand_int()])

    list1.append({"priority": 1, "task": "random values"})
    print(list1[10].values())

if __name__ == "__main__":
    main()