class Bank:
    def __init__(self, bankName):
        self.bankName = bankName 
        self.accounts = []

    def openAccount(self, account):
        self.accounts.append(account)
        print(f'Your new bank account {account.getAccountNumber()} has been opened!')

    def searchAccount(self, accountNumber):
        for account in self.accounts:
            if account.getAccountNumber == accountNumber:
                return account
        
class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance

    def getAccountNumber(self):
        return self.accountNumber
    
    def getAccountHolderName(self):
        return self.accountHolderName
    
    def getRateOfInterest(self):
        return self.rateOfInterest
    
    def getCurrentBalance(self):
        return self.currentBalance
    
    def setAccountHolderName(self, newName):
        self.accountHolderName = newName

    def setRateOfInterest(self, newRate):
        self.rateOfInterest = newRate

    def deposit(self, amount):
        if amount > 0:
            self.currentBalance += amount
            print(f'Deposit  successful, Your new balance is: {self.currentBalance}')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.currentBalance:
            self.currentBalance -= amount
            print(f'Widthdrawl successful, Your new balance is: {self.currentBalance}.')
        else:
            print('Invalid deposit amount')

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.minimumBalance = minimumBalance 

    def widthdraw(self, amount):
        if amount > 0 and (self.currentBalance - amount) >= self.minimumBalance:
            super().withdraw(amount)
        else:
            print('Invalid withdrawl amount')

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
         super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
         self.overdraftLimit = overdraftLimit

    def widthdraw(self, amount):
        if amount > 0 and (self.currentBalance - amount) >= self.overdraftLimit:
            super().withdraw(amount)
        else:
            print('Invalid withdrawl amount')
