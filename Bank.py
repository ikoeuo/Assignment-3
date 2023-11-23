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
        
    
