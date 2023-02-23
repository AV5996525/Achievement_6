#Name:          achieve_6.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 23, 2023
#Purpose: User is able to input a list of numbers and will have inputed numbers sorted as prime or non prime numbers.
#
#This program will output the user generated number list as either prime or non prime numbers seperately. 
numbers = (input("Enter your numbers")).split(",")
for x in (numbers):
    x = int(x)
    flag = False
    if x == 1:
        print("The number {} is not a prime number".format(x))
        
    elif x > 1 :
        for i in range(2, x) :
            if (x % i) == 0:
                flag = True
                break
        if flag:
            print("The number {} is not a prime number".format(x))
            
        else:
            print("The number {} is a prime number".format(x))
            
