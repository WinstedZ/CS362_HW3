number=int(input("Please enter an integer to determine if that year is a leap year:"))

if(number%4==0):
    if(number%100==0):
        if(number%400==0):
            print(number,"is a leap year.")
        else:
            print(number,"is not a leap year.")
    else:
        print(number,"is a leap year.")
else:
    print(number,"is not a leap year.")

input("Press enter key to exit")