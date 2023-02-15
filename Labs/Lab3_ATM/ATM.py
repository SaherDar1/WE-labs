from Utils import print_header
from DB import DBHandler
from Customer import Customer
from Exceptions import *
import os

# ATM class
class ATM:
    def __init__(self):
        '''
            This function(constructor) is used to initialize the ATM class
        '''
        self.__customers = None

    @property
    def customers(self):
        if self.__customers is None:
            self.__read_customers()
        return self.__customers

    def __read_customers(self):
        '''
            This function is used to read customers from database.
        '''
        db = DBHandler()
        db.connect()
        self.__customers = db.select("select * from customers")


    def __get_customer(self, account_number, pin):
        '''
            Gives a customer object if account number and pin matches
        '''
        for customer in self.customers:
            if customer.account_no.lower() == account_number.lower() and customer.password == pin:
                return customer
        return None

    def __insert_customer(self, customer):
        '''
            This function is used to insert customer to database
            @params: customer
            @return: None
        '''
        db = DBHandler()
        db.connect()
        db.insert("insert into customers(account_no, password, balance) values(%s,%s,%s)", (customer.account_no, customer.password, customer.account_balance))

    def __update_balance(self, account_no, balance):
        '''
            This function is used to update balance of customer
            @params: account_no, balance
            @return: None
        '''
        db = DBHandler()
        db.connect()
        db.update("update customers set balance=%s where account_no=%s", (balance, account_no))

    def register(self):
        '''
            This function is used to register a new customer
            @params: None
            @return: None
        '''
        try:
            print_header('Register your account')

            # load customers
            self.__read_customers()

            # setting automated account number
            account_number = 'ATMAcc1'
            if self.__customers not in [None, []]:
                account_number = 'ATMAcc' + str(int(self.__customers[-1].account_no[-1]) + 1)
            print("Your account number is: ", account_number)

            pin = input('Enter your pin: ')
            if len(pin) != 4 or not pin.isnumeric():
                raise InvalidPin("Pin must be 4 character numberical value")

            balance = 100  # default balance

            # insert the newly created customer to the database.
            customer = Customer(account_number, pin, balance)
            self.__insert_customer(customer)

            # clear the screen
            os.system('cls')
            print_header('Account created successfully')
            self.login() # redirect to login page
        except InvalidPin as e:
            print(str(e)) 
            self.register() # redirect to register page
        except ValueError as e:
            print(str(e))
            self.register() # redirect to register page

    def login(self):
        '''
            This function is used to login a customer
        '''
        # load customers
        self.__read_customers()

        print_header("Login to your account")
        try:
            account_number = input('Enter your account number: ')
            pin = input('Enter your pin: ')
            customer = self.__get_customer(account_number, pin)

            if customer is None:
                raise AccountNotFound("Invalid account no. or pin.")
            try:
                choice = 1
                while True:
                    print()
                    print("-"*40)
                    print(('Welcome ' + customer.account_no).center(40))
                    print("-"*40)
                    print('1. Check Balance')
                    print('2. Withdraw')
                    print('3. Deposit')
                    print('4. Sign Out')
                    print('5. Exit')
                    print("-"*40)
                    try:
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            self.__check_balance(customer)
                        elif choice == 2:
                            self.__withdraw(customer)
                        elif choice == 3:
                            self.__deposit(customer)
                        elif choice == 4:
                            print_header('Signed out successfully')
                            os.system('cls')
                            self.login()
                            break
                        elif choice == 5:
                            print_header('Thank you for using ATM')
                            exit()
                        else:
                            print('Invalid choice')
                    except ValueError as e:
                        print(str(e))
                        self.login()
            except ValueError as e:
                pass
        except AccountNotFound as e:
            print(str(e))
            self.login()
        except ValueError as e:
            print(str(e))
            self.login()

    def __check_balance(self, customer):
        '''
            This function is used to check balance of customer
            @params: customer
            @return: None
        '''
        print_header("Your balance is PKR " + str(customer.account_balance))

    def __withdraw(self, customer):
        '''
            This function is used to withdraw money from customer
            @params: customer
            @return: None
        '''
        try:
            print_header("Your balance is PKR " + str(customer.account_balance))
            amount = float(input('Enter the amount to withdraw: '))
            if amount > customer.account_balance:
                raise InsufficientBalance('Insufficient balance')
            if amount < 0:
                raise ValueError('Invalid amount')

            customer.account_balance -= amount
            print_header('Success! Your new balance is PKR ' + str(customer.account_balance))

            self.__update_balance(customer.account_no , customer.account_balance)

        except InsufficientBalance as e:
            print(str(e))
        except ValueError:
            print('Invalid amount')

    def __deposit(self, customer):
        '''
            This function is used to deposit money to customer
            @params: customer
            @return: None
        '''
        try:
            print_header("Your balance is PKR " + str(customer.account_balance))

            amount = float(input('Enter the amount to deposit: '))
            if amount < 0:
                raise ValueError('Invalid amount')
            customer.account_balance += amount

            print_header('Success! Your new balance is PKR ' + str(customer.account_balance))
            self.__update_balance(customer.account_no , customer.account_balance)
        except ValueError:
            print('Invalid amount')