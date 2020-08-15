#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basic class with example

class Account:
	Income = 0
	Balance = 0
	Expenses = 0
	InterestRate = 0
	MonthlyInterest = 0
	def __init__(self, balance):
		self.Balance = balance
	
	def deposit(self, amount):
		self.Balance += amount;
	
	def withdraw(self, amount):
		self.Balance -= amount
	
	def changeInterestRate(self, newInterest):
		self.InterestRate = newInterest/100
		self.MonthlyInterest = self.InterestRate/12 # Assume compounding is monthly
	
	def elapseTime(self, timeSteps, period):
        
		if period == 'years':
			self.Balance = self.Balance*(1 + self.MonthlyInterest)**(timeSteps*12)
		elif period == 'months':
			self.Balance = self.Balance*(1 + self.MonthlyInterest)**timeSteps
		else:    
			raise Exception('"period" should take the value "years" or' + \
			'"months". The value of "period" was: "' + str(period) + '".')

	def printDetails(self):
		print('Current Balance: R%.2f' % self.Balance +'\n'\
		'Interest Rate: ' + str(self.InterestRate * 100) + '% \n \n')
	
	def annuityFV(self, deposit, term):
		annuityValue = deposit*((1 + self.MonthlyInterest)**term -1)/(self.MonthlyInterest)
		self.Balance = self.Balance*(1 + self.MonthlyInterest)**term + annuityValue

	def annuityPV(self, loanAmt, term):
		self.Balance += loanAmt
		self.Expenses += loanAmt(()/self.MonthlyInterest)


class Loan:
	Amount = 0
	InterestRate = 0
	MonthlyInterestRate = 0
	LoanTerm = 0
	MinMonthlyPayment = 0
	NumTermsPassed = 0
	PaidToDate = 0
	BalanceOutstanding = 0
	
	def __init__(self, amount, interestRate, term):
		self.Amount = float(amount)
		self.InterestRate = interestRate/100
		self.MonthlyInterestRate = self.InterestRate/12
		self.LoanTerm = term*12 # "term" in years
		self.MinMonthlyPayment = amount*((1 - (1 + self.MonthlyInterestRate)**(-self.LoanTerm))/self.MonthlyInterestRate)**-1
		self.BalanceOutstanding = float(amount)
	
	def printDetails(self):
		print('Loan Amount: R%.2f' % self.Amount +'\n' + \
		'Interest Rate: ' + str(self.InterestRate*100) + '% \n' + \
		'Minimum Payment (monthly): R%.2f' % self.MinMonthlyPayment + '\n' + \
		'Balance Outstanding: R%.2f' % self.BalanceOutstanding + '\n' + \
		'Amount Paid to Date: R%.2f' % self.PaidToDate + '\n' + \
		'Remaining Terms: ' + str(self.LoanTerm - self.NumTermsPassed) + '\n')
	
	def regularPayment(self, payment, numPayments):
		if self.MinMonthlyPayment > payment:
			raise Exception('Payment entered is less than minimum payment. ' + \
			'Minimum payment amount is R%.2f' % self.MinMonthlyPayment + '.')
		else:
			self.NumTermsPassed += numPayments
			self.PaidToDate += payment*numPayments
			self.BalanceOutstanding = payment*(1-(1+self.MonthlyInterestRate)**-(self.LoanTerm - self.NumTermsPassed))/self.MonthlyInterestRate