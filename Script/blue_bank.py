# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:59:14 2023

@author: franc
"""

# Importing libraries
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 to read json data
with open('loan_data_json.json') as json_file:
 data = json.load(json_file)
 
# Transforming to dataframe
 df_loan = pd.DataFrame(data)
 
# Checking  data type
df_loan.dtypes

# Finding unique values for the purpose column
df_loan['purpose'].unique()

# Using the describe function
df_loan.describe()

# Describing the data for specific colums
df_loan['int.rate'].describe()
df_loan['fico'].describe()
df_loan['dti'].describe()

# Using EXP() to get the annual income
income = np.exp(df_loan['log.annual.inc'])

# Showing values of log.annual.inc column
df_loan['log.annual.inc'].head(10)

# Using EXP() of numpy to get real income from log.annual.inc column
income = np.exp(df_loan['log.annual.inc'])

# Adding income to column in data_loan
df_loan['annual_income'] = income
df_loan['annual_income'].head(10)

# Showing FICO column
df_loan['fico'].head(10)

# Grouping FICO Scores

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

# Applying for loops to loan data


length = len(df_loan)
ficocat = []
for x in range(0, length):
    category = df_loan['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category <= 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 780:
        cat = 'Good'
    else:
        cat = 'Excellent'
    ficocat.append(cat)

# Adding series to df_loan

fico = df_loan['fico']
ficocat = pd.Series(ficocat)
df_loan['fico_category'] = ficocat

# Showing the number of borowers by fico_category
category_plot = df_loan.groupby(['fico_category']).size()
category_plot.plot.bar(color='green', width = 0.3)
plt.show()

# For interest rate, a new column is wanted. rate <0.12 then high, else low

df_loan.loc[df_loan['int.rate'] > 0.12, 'int.rate.type'] = 'High'           
df_loan.loc[df_loan['int.rate'] <= 0.12, 'int.rate.type'] = 'Low' 

# Showing the number of loans/rows by purpose

purposecount= df_loan.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.5)
plt.show()

# Showing a scatterplot

ypoint = df_loan['log.annual.inc']
xpoint = df_loan['dti']
plt.scatter(xpoint, ypoint, color = 'orange')
plt.show

# Exporting to csv
df_loan.to_csv('loan_clean.csv', index = True)
