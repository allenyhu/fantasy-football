#%%
import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/allenhuang/fantasy-football/ltcwff_files/data'

pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))  # adp data
# %%

pg['total_yards1'] = pg['rush_yards'] + pg['pass_yards'] + pg['rec_yards']
pg['total_yards2'] = (pg[['rush_yards', 'pass_yards', 'rec_yards']]).sum(axis=1)
print(pg['total_yards1'].head())
print(pg['total_yards2'].head())

# %%

print(pg[['rush_yards', 'rec_yards']].mean())

pg['good_pass_game'] = (pg['pass_yards'] >= 300) & (pg['pass_tds'] >= 3)
num_good_pass_game = pg['good_pass_game'].sum()
print(num_good_pass_game)
print(num_good_pass_game / (pg['pos'] == 'QB').sum())

print(pg['rush_tds'].sum())

week_counts = pg['week'].value_counts()
print(week_counts.max())
print(week_counts.min())
# %%