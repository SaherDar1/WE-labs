from ATM import ATM
from Utils import print_header

def main():
    '''
        This function is used to run the program
        @params: None
        @return: None
    '''
    print_header('Welcome to ATM')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    print("-"*40)

    # Creating an ATM instance (to manage the ATM)
    atm = ATM()

    choice = 1
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                atm.register() # Registering a new customer
            elif choice == 2:
                atm.login() # Logging in a customer
            elif choice == 3:
                print_header('Thank you for using ATM')
                break
            else:
                raise ValueError('Invalid choice')
        except ValueError as e:
            print('Invalid choice: ' + str(str(e)))
            continue

# call to main function
if __name__ == '__main__':
    main()
