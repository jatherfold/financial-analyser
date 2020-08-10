#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basic class with example

class Account:
	Balance = 0
	InterestRate = 0
	def __init__(self, balance):
		self.Balance = balance
	
	def deposit(self, amount):
		self.Balance += amount;
	
	def withdraw(self, amount):
		self.Balance -= amount
	
	def changeInterestRate(self, newInterest):
		self.InterestRate = newInterest/100 # Assume compounding is monthly
	
	def elapseTime(self, timeSteps, period):
		intRate = self.InterestRate
        
		if period == 'years':
			self.Balance = self.Balance*(1 + intRate/12)**(timeSteps*12)
		elif period == 'months':
			self.Balance = self.Balance*(1 + intRate/12)**timeSteps
		else:    
			raise Exception('"period" should take the value "years" or' + \
			'"months". The value of "period" was: "' + str(period) + '".')

	def printDetails(self):
		print('Current Balance: R%.2f' % self.Balance +'\n'\
		'Interest Rate: ' + str(self.InterestRate * 100) + '% \n \n')
	
	def annuityFV(self, deposit, term):
		monthlyInterest = self.InterestRate/12
		annuityValue = deposit*((1 + monthlyInterest)**term -1)/(monthlyInterest)
		self.Balance = self.Balance*(1 + monthlyInterest)**term + annuityValue