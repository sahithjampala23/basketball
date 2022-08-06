import pandas as pd
import numpy as np
from uuid import uuid4

rosters_df = pd.read_csv('data/rosters_all_time.csv')

players = rosters_df.groupby(['PLAYER', 'BIRTH_DATE']).agg({'POS':'last', 'HEIGHT':'last', 'WEIGHT':'last', 'NATIONALITY':'last', 'EXPERIENCE':'last', 'COLLEGE':'last'}).reset_index()

for name, dob in zip(players['PLAYER'],players['BIRTH_DATE']):
    players.loc[(players['PLAYER'] == name) & (players['BIRTH_DATE'] == dob), 'UUID'] = str(uuid4())

players[['UUID', 'PLAYER', 'BIRTH_DATE', 'POS', 'EXPERIENCE','HEIGHT', 'WEIGHT', 'NATIONALITY', 'COLLEGE']].to_csv('data/players_all_time.csv')