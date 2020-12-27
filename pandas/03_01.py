#%%
import pandas as pd
from os import path

DATA_DIR = '/Users/allenhuang/Desktop/ltcwff_files/data'
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))

#%%
# Use the adp DataFrame to create another DataFrame, 
# adp50, that is the top 50 (by ADP) players.
adp50 = adp.head(50)
adp50.shape

#%%
# Sort adp by name in descending order (so Zay Jones is on the first line).
# On another line, look at adp in the REPL and make sure it worked.
adp.sort_values('name', ascending=False)

#%%
# What is the type of adp.sort_values('adp')?
type(adp.sort_values('adp'))

#%%
"""
a) Make a new DataFrame, adp_simple, with just the columns 
   'name', 'position', 'adp' in that order.
b) Rearrange adp_simple so the order is 'pos', 'name', 'adp'.
c) Using the original adp DataFrame, add the 'team' column to adp_simple.
d) Write a copy of adp_simple to your computer, ‘adp_simple.txt’ 
   that is '|' (pipe) delimited instead of ',' (comma) delimited.
"""
adp_simple = adp[['name', 'position', 'adp']]
adp_simple.head()

adp_simple = adp_simple[['position', 'name', 'adp']]
adp_simple.columns = ['pos', 'name', 'adp']
adp_simple.head()

adp_simple['team'] = adp['team']
adp_simple.head()

adp_simple.to_csv(path.join(DATA_DIR, 'adp_simple.txt'), sep='|')
# %%
