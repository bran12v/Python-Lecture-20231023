# Lists in python are essentially sequences of values, collections of elements
# [a, b, c, d]
# a is at index 0, b is at index 1, etc etc

a = 4
b = 3
c = 2
d = 1
firstlist = [a, b, c, d] # list of variables
secondlist = ["a", "b", "c", "d"] # list of strings
# print(firstlist)
# print(secondlist)

# 0 -> length of the list - 1
complexList = [1, "a", ["D", "C", "G"], True, 2.0, {"Hello": "World"}]
# print(complexList)
# print(type(complexList))

# Get a specific item in my list
# Access its index
# 0 -> 5
# print(len(complexList))
# You can access an index by using [indexNumber]
# print(complexList[3])
# print(complexList[2][1])

# Change items in a list
complexList[3] = False
# print(complexList)

# add items to a list
# use a function called .append(insert items here)
complexList.append("Brandon")
complexList.append("Mayito")
complexList.pop(7)
del complexList[6]

# If you want to add to a specific location, use insert(index, value)
complexList.insert(0, "Joshua")

# print(complexList)

# Functions we can use with list
"""
len() - gets the length of the list
    ex: len(list) => 5 

max() or min() - this finds the maximum or minimum values respectively of a list of numbers
    max([1,2,3,3,4,5,6]) = 6
    min([1,2,3,3,4,5,6]) = 1

index() - find the index of a value in my list
    list.index(value) - this will give me the index of the FIRST time that value shows up in my list
    
count() - count the number of times something shows up in a list
    [1,2,3,3,4,5,6].count(3) = 2

extend() - add lists togther into the current list
    complexList.extend(firstlist)

clear() - delete everything

sort() - sorts your list

copy() - copies one list to another

remove() - remove first instance of value from list
    list.remove(value)
"""
# list1 = ["asdas", "Brandon", "Jon", "Brandon"]
# print(list1.index("Brandon"))
# print(complexList)
# firstlist.extend(complexList)
# print(firstlist)
# list1 = ["c", "a", "d", "b", "g"]
# list1.sort(reverse=True)
# print(list1)
# list1 = complexList.copy()
# print(list1)

list1 = [1,2,3,4,5,6]
for i in range(len(list1)):
    list1[i] += 2
    print(list1[i])