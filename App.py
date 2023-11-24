from Bank import Bank
from Bank import SavingsAccount
from Bank import ChequingAccount

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
    bank = Bank('RBC')
    
    while True:
        showMainMenu()
        choice = int(input('Enter choice: '))
        
        if choice == 1:
            accountType = input("Enter account type: ").lower()
            accountNumber = int(input("Enter account number: "))
            accountHolderName = input("Enter account holder name: ")
            rateOfInterest = float(input("Enter rate of interest: "))
            initialBalance = float(input("Enter initial balance: "))
            
            if accountType == 'Savings':
                minimum_balance = float(input("Enter minimum balance for Savings Account: "))
                account = SavingsAccount(accountNumber, accountHolderName, rateOfInterest, initialBalance, minimum_balance)
            elif accountType == 'Chequing':
                overdraft_limit = float(input("Enter overdraft limit for Chequing Account: "))
                account = ChequingAccount(accountNumber, accountHolderName, rateOfInterest, initialBalance, overdraft_limit)
            else:
                print("Invalid account type.")
            Bank.openAccount(account)

        elif choice == 2:
              accountNumber = int(input('Enter your account number: '))  
              if accountNumber is account:
                   while True:
                        showAccountMenu()
                        accountChoice = int(input('What would you like to select: '))

                        if accountChoice == 1:
                             amount = float(input('How much money would you like to deposit? '))
                             account.deposit(amount)

                        elif accountChoice == 2:
                            amount = float(input('How much money would you like to withdraw? '))
                            account.withdraw(amount)

                        elif accountChoice == 3:
                            print(f'Your current balance: {account.getCurrentBalance()}')
                        elif accountChoice == 4:
                             break
                        else:
                             print('Please select a valid choice')
                
              else:
                print('404 Account not found')

        elif choice == 3:
            print('Goodbye, thank you for using our app!')
            break

while True:
    run()