""" 
    Write a program that analyzes the entered number and, depending on the number, 
    gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
    Take into account cases of entering numbers from 8 and more,
    as well as cases of entering nonnumerical data.
"""

def check_day(day):
    if day < 1 or day > 7:
        raise ValueError("Day can't be less than 1 or more than 7")
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

def main():
    try:
        day = int(input("Enter number of the day: "))
        check_day(day)
    except ValueError as e:
        print("We obtained an error:", e)

if __name__ == "__main__":
    main()  