# Take user input
name = input("Enter name: ")
age = input("Enter age: ")

var1=1
while var1==1:
    try:
        age_int = int(age)

        if age_int<0:
            print("Age cannot be negative value")
        else:
            print("Hello: ", name )
            if age_int<13:
                print("You are a Child")
                print("You are not eligible to vote")
            elif 13<=age_int<=17:
                print("You are a Teenager")
                print("You are not eligible to vote")
            elif 18<=age_int<=59:
                print("You are an Adult")
                print("You are eligible to vote")
            else:
                print("You are a Senior Citizen")
                print("You are eligible to vote")
            
    except:
        print("Please enter age valid input")
        var1=0
    break
