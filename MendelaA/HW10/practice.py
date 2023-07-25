class BankAccount():
    def __init__ (self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self._balance = balance
    
    @property
    def account_holder(self):
        return self.__account_holder
    
    @account_holder.setter
    def get_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def deposit(self, deposite_sum):
        self._balance += deposite_sum
        return self._balance

    def withdraw(self, withdraw_sum):
        if ((self._balance - withdraw_sum) <= 0):
            print(f'Insufficient funds')
        else:
            self._balance -= withdraw_sum
            # print(self._balance)
            return self._balance

    def check_balance(self):
        return self._balance



def test_bank_account():
    # Test creating a BankAccount
    my_account = BankAccount("123456789", "John Doe", 1000.0)
    assert my_account.account_holder == "John Doe"
    try:
        _ = my_account.account_number
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

    # Test checking the balance
    assert my_account.check_balance() == 1000.0

    # Test depositing money
    my_account.deposit(500.0)
    assert my_account.check_balance() == 1500.0

    # Test withdrawing money
    my_account.withdraw(250.0)
    assert my_account.check_balance() == 1250.0


    # Test withdrawing too much money
    my_account.withdraw(3000.0)
    assert my_account.check_balance() == 1250.0


    # Test setting account holder
    try:
        my_account.account_holder = "Jane Doe"
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

test_bank_account()