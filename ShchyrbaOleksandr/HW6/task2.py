log = input("Register with your email: ")
while True:
    logins = input("Enter your email: ")
    if logins == log:
        print("Hello, dear user!")
        break
    else:
        print("Errore! Wrong email!")
