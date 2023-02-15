from Exceptions import InvalidPin, NegativeNumberException, InvalidAccountType, AccountNotFound
from User import User


class Account(User):
    def __init__(self, accountno, password, interest, balance=100, transactions=0, type="charity"):
        User.__init__(self, accountno, password,
                      interest, balance, transactions)
        self.type = type

    def inputPin():
        success = True
        while success:
            try:
                pin = int(input("Enter your pin : "))
                if (pin < 0):
                    raise NegativeNumberException("Error : Pin is negative")
                str1 = str(pin)
                if (len(str1) != 4):
                    raise InvalidPin("Error : Pin length is not equal to 4")
                success = False
            except Exception as e:
                print(str(e))
        return pin

    def inputAccount():
        accountno = input("Enter account no: ")
        password = Account.inputPin()
        transactions = 0
        interest = 0
        type = input("Enter account type : ")
        if (type == "basic bank account"):
            account = Account(accountno, password, 0, 100,
                              4, "basic bank account")
            return account
        elif (type == "current account"):
            account = Account(accountno, password, 0, 100,
                              10000, "current account")
            return account
        elif (type == "savings account"):
            account = Account(accountno, password, 0, 100,
                              10000, "saving account")
            return account
        else:
            raise InvalidAccountType("Invalid account type")
