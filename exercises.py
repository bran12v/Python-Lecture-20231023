"""  
9. Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
0 + 1 = 1 + 1 = 2 + 1 = 3 + 2 = 5
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""

num1 = 0
num2 = 1

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5

while num2 < 50:
    print(num2)
    temp = num2 
    num2 = num1 + num2 
    num1 = temp 
    
"""  
2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
while True:
    temperatureType = input("Celcius or Fahrenheit (c or f): ")
    if temperatureType != "c" and temperatureType != "f":
        print("You dummy, I said c or f")
    else:
        tempVal = int(input("What is the tempurature? "))
        if temperatureType == "c":
            # temp * (9/5) + 32 
            tempVal = tempVal * (9/5) + 32
            print("The temp in Fahrenheit is: ", tempVal)

        if temperatureType == "f":
            # (temp - 32) * 5/9
            tempVal = (tempVal - 32) * (5/9)
            print("The temp in Celcius is: ", tempVal)
            
    cont = input("Do you want to continue: y or n: ")
    if cont == "y":
        continue
    else:
        break