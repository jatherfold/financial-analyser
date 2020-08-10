#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:56:50 2020

Example Script for Account Class

@author: john
"""

import Analyser

savings = Analyser.Account(70000)
savings.changeInterestRate(3.75)
savings.printDetails()
savings.annuityFV(8000, 24)
savings.printDetails()

apartment = Analyser.Loan(1000000.00,6.5,20)
apartment.printDetails()