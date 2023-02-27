#Name:          achieve_6.py
#Author:        AJ Varatharajan
#Date Created:  February 22, 2023
#Date Last Modified: February 26, 2023
#Purpose: User is able to input a list of numbers and will have inputed numbers sorted as prime or non prime numbers.
#
#This program will output the user generated number list as either prime or non prime numbers seperately. 
numbers = (input("Enter your numbers list seperated by a comma:")).split(",") #creating variable to store user's numbers, each number must be seperated with the comma during input.
NP = "" #Establishing non prime number list
PN = "" #Establishing prime number list
for x in (numbers): #cycling through each entry in numbers list
    x = int(x) #converting strings into integers from each entry in numbers
    flag = False #intializing flag
    if x == 1: #condition of value that makes it a prime number
        print("The number {} is not a prime number".format(x))
        NP += str(x)
    elif x > 1 : # other condition which can make the value prime or non prime
        for i in range(2, x) : #cycling through each value that is from 2 to any number greater than 1
            if (x % i) == 0: # if no remainder
                flag = True #Flag condition active and will break out of the loop 
                break
        if flag: # If flag is true
            print("The number {} is not a prime number".format(x)) #Identify which number is non prime
            NP += str(x) #Add the entry of a non prime number to non prime list
        else: #If there is a remainder
            print("The number {} is a prime number".format(x)) #Identify which number is a prime number
            PN += str(x) #Add entry to prime number list
NPsep = [int(i) for i in str(NP)] #cycling through each number and seperating each number in the non prime list and saving it to a seperated list of non prime numbers
print("The following numbers are non prime numbers: ", NPsep) #printing seperated version of non prime number list
PNsep = [int(i) for i in str(PN)]  #cycling through each number and seperating each number in the non prime list and saving it to a seperated list of prime numbers
print("The following numbers are prime numbers: ", PNsep) #printing seperated version of prime number list