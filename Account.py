# Basic class with example

class Account:
    def __init__(self, balance):
        self.Balance = balance
        self.InterestRate = 0
        
    def deposit(self, amount):
        self.Balance += amount
        
    def withdraw(self, amount):
        self.Balance -= amount
        
    def changeInterestRate(self, newInterest):
        self.InterestRate = newInterest/100 # Assume compounding is monthly
        
    def elapseTime(self, timeSteps, period):
        intRate = self.InterestRate;
        
        if period == 'years':
            self.Balance = self.Balance*(1 + intRate/12)**(timeSteps*12)
        elif period == 'months':
            self.Balance = self.Balance*(1 + intRate/12)**timeSteps
        else:    
            raise Exception('"period" should take the value "years" or \
            "months". The value of "period" was: ' + str(period))
            
    def printDetails(self):
        print('Current Balance: R%.2f' % self.Balance +'\n'\
        'Interest Rate: ' + str(self.InterestRate * 100) + '% \n \n')

savings = Account(0)
savings.deposit(10000)
savings.printDetails()
savings.changeInterestRate(3.75)
savings.printDetails()
savings.elapseTime(3,'month')
savings.printDetails()