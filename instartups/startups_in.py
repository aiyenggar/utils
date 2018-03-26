#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 05:43:32 2018

@author: aiyenggar
"""

import sys
import os
from datetime import datetime
import subprocess
import csv
import numpy as np
import pandas as pd


file_company="/Users/aiyenggar/data/tracxn/Geo India Company Details(Cleaned).xls"
file_funding="/Users/aiyenggar/data/tracxn/Geo India Funding data(Cleaned).xls"

company = pd.read_excel(file_company)
funding = pd.read_excel(file_funding)

funding.info()

funding.describe()

funding['RoundName'].unique()
len(funding['CompanyName'].unique()) # 3657 companies, total 10020 entries

#print(len(funding[funding['RoundName'].str.contains("Series A")].index.values[:]))

# Grab DataFrame rows where column has certain values
otherearlylist = ['Grant', 'Equity Crowdfunding']
earlylist = ['Angel', 'Seed', 'Series A']
early = funding[funding.RoundName.isin(earlylist)]
midlist = ['Series B', 'Series C', 'Series D']
latelist = ['Series E', 'Series F', 'Series G', 'Series H', 'Series I', 'Series J']
publist = ['PE', 'Post IPO']
debtlist = ['Debt', 'ConvertibleDebt']

simplefunding = funding[['FundingYear', 'FundingAmount', 'Currency', 'RoundName']].dropna()

# Make FundingAmount a number
simplefunding['FundingAmount'] = pd.to_numeric(simplefunding['FundingAmount'], errors='coerce')
# Get all currency in USD
simplefunding['Currency'].unique() # INR and USD
inr = simplefunding[simplefunding.Currency.isin(['INR'])]
simplefunding = simplefunding[simplefunding['Currency'] == 'USD']
# Make year a number
simplefunding['FundingYear'] = simplefunding['FundingYear'].astype(int)
simplefunding = simplefunding[simplefunding['FundingYear'] > 2005]

fundingseries = simplefunding.groupby(['FundingYear', 'RoundName'])['FundingAmount'].sum()
#plot_df = fundingseries.unstack('RoundName')



import matplotlib
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
plt.figure()

early = simplefunding[simplefunding.RoundName.isin(earlylist)]
early.groupby(['FundingYear','RoundName'])['FundingAmount'].sum().unstack().plot()

mid = simplefunding[simplefunding.RoundName.isin(midlist)]
mid.groupby(['FundingYear','RoundName'])['FundingAmount'].sum().unstack().plot()

late = simplefunding[simplefunding.RoundName.isin(latelist)]
late.groupby(['FundingYear','RoundName'])['FundingAmount'].sum().unstack().plot()

pub = simplefunding[simplefunding.RoundName.isin(publist)]
pub.groupby(['FundingYear','RoundName'])['FundingAmount'].sum().unstack().plot()

debt = simplefunding[simplefunding.RoundName.isin(debtlist)]
debt.groupby(['FundingYear','RoundName'])['FundingAmount'].sum().unstack().plot()
#plot_df = fundingseries.unstack('RoundName').loc[:, 'FundingAmount']
# By city, you can get total funding statistics, as well as distribution by funding stage
# You can check the distribution by UnicornFlag
# How much funding has come into various industries by year
# Which firms have absorbed maximum funding
# Which firms have participated in most funding rounds
# For each of the above, their is a year aspect
# Who are the investors entering at advanced investment rounds

"""
funding_round = funding.groupby('RoundName')
type(funding_round)
funding_round.describe()


Angel	1479
ConvertibleDebt	29
Debt	292
Equity-Crowdfunding	5
Grant	191
PE	450
Post-IPO	102
Seed	3289
Series-A	1673
Series-B	774
Series-C	297
Series-D	118
Series-E	53
Series-F	20
Series-G	11
Series-H	10
Series-I	6
Series-J	2
Unattributed	6
"""
