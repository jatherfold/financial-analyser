#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:56:50 2020

Example Script for Account Class

@author: john
"""

import Analyser

current = Analyser.Account(10000)
current.increase(25000, 'Income')
current.increase(5000, 'Expense')
current.printDetails()
current.elapseTime(5)
current.printDetails()

apartment = Analyser.Loan(829000,10.25,20)
apartment.printDetails()
apartment.regularPayment(apartment.MinMonthlyPayment, 5)
apartment.printDetails()

savings = Analyser.Investment(30000, 3.75)
savings.regularPayment(5000,10)
savings.printDetails()
savings.elapseTime(5)
savings.printDetails()