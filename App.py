import Bank

def showMainMenu():
    print('Would you like to:')
    print('1. Open a new account')
    print('2. Access an account')
    print('3. Exit')

def showAccountMenu():
    print('1. Deposit into an account')
    print('2. Withdraw from an account')
    print('3. Check account balance')
    print('4. Go back to the main menu')

def run():
    bank = Bank(input('Enter bank name: '))

    