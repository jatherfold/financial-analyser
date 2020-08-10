#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:56:50 2020

Example Script for Account Class

@author: john
"""

from Analyser import Account

#savings = Account(0)
#savings.deposit(10000)
#savings.printDetails()
#savings.changeInterestRate(3.75)
#savings.printDetails()
#savings.elapseTime(3,'months')
#savings.printDetails()

savings = Account(70000)
savings.changeInterestRate(3.75)
savings.printDetails()
savings.annuityFV(8000, 24)
savings.printDetails()
