import unittest
import Analyser

class TestAccountMethods(unittest.TestCase):

	def testDeposit(self):
		initialValue = 0
		depositValue = 10000
		account = Analyser.Account(initialValue)
		account.deposit(depositValue)
		self.assertEqual(account.Balance, depositValue + initialValue)
	
	def testWithdrawal(self):
		initialValue = 20000
		depositValue = 10000
		account = Analyser.Account(initialValue)
		account.withdraw(depositValue)
		self.assertEqual(account.Balance, initialValue - depositValue)
	
	def testIncreaseIncome(self):
		initialValue = 0
		increaseValue = 10000
		account = Analyser.Account(initialValue)
		account.increase(increaseValue, 'Income')
		self.assertEqual(account.Income, increaseValue)
	
	def testIncreaseExpenses(self):
		initialValue = 0
		increaseValue = 10000
		account = Analyser.Account(initialValue)
		account.increase(increaseValue, 'Expense')
		self.assertEqual(account.Expenses, increaseValue)

if __name__ == '__main__':
	unittest.main()