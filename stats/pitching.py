import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type']=='play']

strike_outs = plays[plays['event'].str.contains('K')]

#group by year and game
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

#reset index
strike_outs = strike_outs.reset_index(name='strike_outs')

strike_outs = strike_outs.loc[:,['year', 'strike_outs']].apply(pd.to_numeric)
