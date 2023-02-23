numbers = (input("Enter your numbers")).split(",")
for x in (numbers):
    x = int(x)
    flag = False
    if x == 1:
        print("The number {} is not a prime number".format(numbers))
    elif x > 1 :
        for i in range(2, x) :
            if (x % i) == 0:
                flag = True
                break
        if flag:
            print("The number {} is not a prime number".format(numbers))
        else:
            print("The number {} is a prime number".format(numbers))
