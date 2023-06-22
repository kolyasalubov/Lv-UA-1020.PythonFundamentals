""" 
    Create a class "BankAccount" that implements encapsulation. The class should have the following attributes:
        account_number (string)
        account_holder (string)
        balance (float)
    The class should have the following methods:
        deposit(amount) - a method that allows the account holder to deposit money into the account
        withdraw(amount) - a method that allows the account holder to withdraw money from the account; write "Insufficient funds" if money doesn't enough
        check_balance() - a method that returns the current balance of the account
    The class should also have the following restrictions:
        account_number should not be accessible from outside the class
        balance should not be directly accessible from outside the class, it should only be accessible through the methods deposit() and withdraw()
        account_holder should be accessible from outside the class but should not be modifiable
"""
class BankAccount:
    
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
    
    def check_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"Account number: {self.__account_number}, account holder: {self.__account_holder}, balance: {self.__balance}"
    
    @property
    def account_holder(self):
        return self.__account_holder
