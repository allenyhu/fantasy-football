#%%
import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/allenhuang/Desktop/ltcwff_files/data'

# load data
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

# %%
# Add a column to pg, 'rec_pts_ppr' that gives total receiving fantasy points, 
# where the scoring system is 1 point for every 10 yards receiving, 
# 6 points per receiving TD and 1 point per reception.

pg['rec_pts_ppr'] = (0.1 * pg['rec_yards']) + pg['receptions'] + (6 * pg['rec_tds'])
pg[['player_name', 'rec_yards', 'receptions', 'rec_tds', 'rec_pts_ppr']].sample(5)

# %%
# Add a column 'player_desc' to pg that takes the form, ‘ is the ’, 
# e.g. 'T.Brady is the NE QB' for tom brady

pg['player_desc'] = pg['player_name'] + ' is the ' + pg['team'] + ' ' + pg['pos']
pg['player_desc'].sample(5)

# %%
# Add a boolean column to pg 'is_possesion_rec' indicating whether 
# a players air yards were greater than his total yards after the catch.

pg['is_possession_rec'] = pg['caught_airyards'] > pg['raw_yac']
pg[['player_name', 'is_possession_rec', 'caught_airyards', 'raw_yac']].sample(5)


# %%
# Add a column 'len_last_name' that gives the length of the player’s last name.

pg['len_last_name'] = pg['player_name'].apply(lambda n: len(n[2:]))
pg[['player_name', 'len_last_name']].sample(5)


# %%
# 'gameid' is a numeric (int) column, but it’s not really meant for doing math,
# change it into a string column.

pg['gameid'] = pg['gameid'].astype(str)
type(pg['gameid'][0])

# %%

pg.columns = [col.replace('_', ' ') for col in pg.columns]
pg.columns = [col.replace(' ', '_') for col in pg.columns]
pg.columns

# %%
pg['rush_td_percentage'] = pg['rush_tds'] / pg['carries']

# Some don't have values because that player didn't have a carry
pg['rush_td_percentage'].fillna(-99, inplace=True)

pg[['player_name', 'rush_td_percentage']].sample(5)

# %%
pg.drop('rush_td_percentage', axis=1, inplace=True)
pg.columns