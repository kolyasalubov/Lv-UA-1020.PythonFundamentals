import re

def password(pas: str) -> bool:
    if len(pas)<6 or len(pas)>16 or not re.search('[a-z]',pas)or not re.search('[A-Z]',pas)or not re.search('[0-9]',pas)or not re.search('[$#@]',pas):
        return False
    return True

def main():
    pas = input("Enter your password:")
    if password(pas):
        print("Password is ok")
    else:
        print("Password is not valid...")

#
if __name__ == "__main__":
    main()        