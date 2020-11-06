import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type']=='play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

#convert column Type
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

replacements = {r'^S(.*)': 'single',
r'^D(.*)': 'double',
r'^T(.*)': 'triple',
r'^HR(.*)': 'hr'
}

hit_type = hits['event'].replace(replacements, regex=True)
hits =hits.assign(hit_type=hit_type)
