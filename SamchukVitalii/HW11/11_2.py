def week(day):
    if day < 1 or day > 7:
        raise ValueError("must be in the range 1 to 7..")
    match day: 
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
#
try:
    day = int(input("Enter number of the day: "))
    week(day)
except ValueError as e:
    print("error",e)
##