from Exceptions import *

class Customer:
    def __init__(self, account_no=None, password=None, account_balance=None):
        self.__account_no = account_no
        self.__password = password
        self.__account_balance = account_balance

    # accountbalance getter
    @property
    def account_balance(self):
        return self.__account_balance

    # accountbalance setter
    @account_balance.setter
    def account_balance(self, account_balance):
        self.__account_balance = account_balance

    # accountno getter
    @property
    def account_no(self):
        return self.__account_no

    # accountno setter
    @account_no.setter
    def account_no(self, account_no):
        self.__account_no = account_no

    # password getter
    @property
    def password(self):
        return self.__password

    # password setter
    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        print("Account No: ".ljust(20), self.account_no)
        print("Account Balance: ".ljust(20), self.account_balance)
        print("Password: ".ljust(20), self.password)