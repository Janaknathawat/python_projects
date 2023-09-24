#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas_datareader as pdr
import pandas  as pd 
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


## Downloading and importing the data
data = 'TSLA'


# In[17]:


yf.download(data)


# In[19]:


tsla = yf.download(data)


# In[22]:


tsla.tail()


# In[45]:


# Rearranging the column names
data = pd.DataFrame(tsla)
df_tesla = data[['High','Low','Open','Close','Volume','Adj Close']]
df_tesla.tail()


# In[46]:


type(df_tesla)


# In[49]:


df_tesla['High'].plot(figsize=(12,4))


# In[56]:


## x limit and y limit
df_tesla['High'].plot(xlim = ['2022-01-01','2023-09-11'],figsize=(12,4))


# In[60]:


df_tesla['High'].plot(xlim = ['2022-01-01','2023-09-11'],ylim = [100,500], figsize=(12,4), c='green')


# In[62]:


df_tesla.index


# In[67]:


## Reviewing data of specific date range
index = df_tesla.loc['2022-01-01':'2023-09-11'].index
share_open = df_tesla.loc['2022-01-01':'2023-09-11']['Open']


# In[68]:


share_open


# In[69]:


index


# In[78]:


## Subplot on share open prize
figure,axis=plt.subplots()
plt.tight_layout()
figure.autofmt_xdate()
axis.plot(index,share_open)


# ## Datetime Index

# In[80]:


df_tesla = df_tesla.reset_index()


# In[82]:


df_tesla.info()


# In[83]:


df_tesla.tail()


# In[84]:


df_tesla = df_tesla.set_index("Date", drop = True)


# In[86]:


df_tesla.tail()


# In[88]:


## year end frequency
df_tesla.resample(rule='A').min()


# In[90]:


df_tesla.resample(rule='A').max()


# In[92]:


df_tesla.resample(rule='A').max()['Open'].plot()


# In[105]:


## Quartly end frequency
df_tesla.resample(rule='QS').max().loc['2019-01-01':'2023-09-11']


# In[97]:


df_tesla.resample(rule='QS').max()['High'].plot(xlim = ['2019-01-01','2023-09-11'])


# In[99]:


## Business End Frequency
df_tesla.resample(rule='BA').max()


# In[100]:


df_tesla.resample(rule='BA').max()['High'].plot(xlim = ['2019-01-01','2023-09-11'])


# In[106]:


## Business End Quartly Frequency
df_tesla.resample(rule='BQS').max().loc['2019-01-01':'2023-09-11']


# In[102]:


df_tesla.resample(rule='BA').max()['High'].plot(xlim = ['2019-01-01','2023-09-11'])


# In[115]:


## Plotting Graphs
df_tesla['Open'].resample(rule='BA').mean().loc['2019-01-01':'2023-09-11'].plot(kind='bar')


# In[116]:


## Monthly share price data
df_tesla['Open'].resample(rule='M').max().loc['2023-01-01':'2023-09-11']


# In[114]:


df_tesla['Open'].resample(rule='M').max().loc['2023-01-01':'2023-09-11'].plot(kind='bar')


# In[118]:


## Aggregate Function
df_tesla['High'].rolling(5).max().head(6)


# In[125]:


df_tesla['Open:30 days rolling'] = df_tesla['Open'].rolling(30).mean()


# In[120]:


df_tesla.head()


# In[126]:


df_tesla[['Open','Open:30 days rolling']].plot(figsize=(12,5))


# In[ ]:




