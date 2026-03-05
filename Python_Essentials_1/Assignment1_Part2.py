# Take user input
number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")

var1=1
while var1==1:
    try:
        int1 = int(number_1)
        int2 = int(number_2)

        if int2==0:
            print("Cannot Divide by zero")
        else:
            print("Sum of the numbers is: ", int1+int2 )
            print("Division of the numbers is: ", int1/int2 )
    except:
        print("Please enter valid input")
        var1=0
    break





