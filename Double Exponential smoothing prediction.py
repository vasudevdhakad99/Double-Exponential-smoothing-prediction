# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:54:09 2023

@author: star26
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:46:00 2023

@author: star26
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# Load data
df=pd.read_excel(r'\\192.168.60.77\dataset_share\BAM_India_SPOT.xls')

df.columns

df.drop(['Price series', 'Price Status', 'Unit of Measure', 
       'Low Price', 'Mid Price', 'High Price', 'Low Price Rs', 'Mid Price Rs',
       'High Price Rs', 'PMI', 'Crude', 'USD','BPCL'] , inplace=True ,axis=1)


df=df[df['Date']>'2023-02-22 00:00:00']



df.head()# Change Month column to datetime and set as index

#df.Month = pd.to_datetime(df.Month)
data = df.set_index('Date')

# Import function
# Import function
from statsmodels.tsa.holtwinters import Holt
# Create and fit a linear model and a dampened model
model = Holt(data)
fit = model.fit()
model2 = Holt(data, damped=True)
fit2 = model2.fit()
# Get predictions
fcast = fit.forecast(8)
fcast2 = fit2.forecast(8)
# Plot time series and the preictions
fig = plt.figure(figsize=(14,6))
plt.plot(data, color='black',)
fcast.plot(color='red', label='Linear Trend', legend=True)
fcast2.plot(color='green', label='Dampened Trend', legend=True)
plt.show()