from DB import DB
from Exceptions import InsufficientBalance, InvalidChoice, NegativeNumberException
from Account import Account


def inputChoiceForLoginMenu():
    success = True
    while success:
        try:
            choice = int(input("Enter your choice : "))
            if (choice < 0 or choice > 4):
                raise InvalidChoice("Error: Select choice 1 to 4")
            success = False
        except ValueError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    return choice


def inputChoiceForLoginSignUp():
    success = True
    while success:
        try:
            choice = int(input("Enter your choice : "))
            if (choice < 0 or choice > 2):
                raise InvalidChoice("Error: Select choice 1 or 2")
            success = False
        except ValueError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    return choice


print("1. Register account")
print("2. Login")
choice = inputChoiceForLoginSignUp()
if (choice == 1):
    acc = Account.inputAccount()
    db = DB()
    if (db.register_account(acc)):
        print("Account registered")
else:
    accountno = input("Enter account no : ")
    password = Account.inputPin()
    db = DB()
    if (db.login(accountno, password)):
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer Amount")
        choice = inputChoiceForLoginMenu()
        balance = db.view_balance(accountno, password)
        if (choice == 1):
            print("Your balance is : ", balance)
        elif (choice == 2):
            money = int(input("Enter money you want to withdraw : "))
            if (money < 0):
                raise NegativeNumberException(
                    "Money can`t be in negative figures")
            if (money > balance):
                raise InsufficientBalance("You have insufficient balance")
            db.adjust_balance(accountno, password, balance - money)
            print("Money withdrawn successfully")
        elif (choice == 3):
            money = int(input("Enter money you want to deposit : "))
            if (money < 0):
                raise NegativeNumberException(
                    "Money can`t be in negative figures")
            db.adjust_balance(accountno, password, balance + money)
            print("Money deposited successfully")
        else:
            money = int(input("Enter money you want to transfer : "))
            if (money < 0):
                raise NegativeNumberException(
                    "Money can`t be in negative figures")
            elif (balance < money):
                raise InsufficientBalance("You have insufficient balance")
            accountno2 = input(
                "Enter account no in which you want to deposit that money : ")
            if (db.isAccountExists(accountno2)):
                db.adjust_balance(accountno, password, balance-money)
                balance = db.get_balance(accountno2)
                db.transfer_amount(accountno2, balance + money)
                print("Money transfered successfully")
            else:
                print("Account not Found")
