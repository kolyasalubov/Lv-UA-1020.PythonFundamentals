def user_age(age):
    if age < 0:
        raise ValueError("You enter a negative number")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")
        
def main():
    try:
        age = int(input("Enter your age: "))
        user_age(age)
    except ValueError :
        print("Error..")

if __name__ == "__main__":
    main()