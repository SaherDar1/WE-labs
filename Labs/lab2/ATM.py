
from fileinput import filename
from Account import Account
from ExceptionClasses import AccountNotFound, InvalidChoice, InvalidPin, NegativeNumberException


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


def inputChoiceForLoginMenu():
    success = True
    while success:
        try:
            choice = int(input("Enter your choice : "))
            if (choice < 0 or choice > 3):
                raise InvalidChoice("Error: Select choice 1 or 2 or 3")
            success = False
        except ValueError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    return choice


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


def registerAccount():
    file = open("input.txt")
    try:
        numRecords = int(file.readline())
        numRecords += 1
        file.close()
        pin = inputPin()
        accountNumber = "ATM"+str(numRecords)
        accountInfo = Account(accountNumber, pin)
        accountInfo.writeInFile(str(numRecords))
    except Exception as e:
        print(str(e))
    finally:
        file.close()


def login():
    accountNo = input("Enter account number : ")
    pin = inputPin()
    file = open("input.txt")
    lines = file.readlines()
    isIteration1 = True
    for item in lines:
        if (isIteration1):
            isIteration1 = False
        else:
            parts = item.split(",")
            account = Account(parts[0], int(parts[1]), int(parts[2]))
            if (accountNo == account.accountNo):
                if (pin == account.pin):
                    return account
                raise InvalidPin("Pin is incorrect")
    raise AccountNotFound("Account with given credentials does not exist")


print("1. Register account")
print("2. Login")
choice = inputChoiceForLoginSignUp()
try:
    if (choice == 1):
        registerAccount()
    else:
        accountObj = login()
        print("1. View balance")
        print("2. Withdraw")
        print("3. Deposit")
        choice2 = inputChoiceForLoginMenu()
        if (choice2 == 1):
            print("Your balance is : ", accountObj.balance)
        elif (choice2 == 2):
            print()
except Exception as e:
    print(str(e))
