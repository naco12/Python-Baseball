import pandas as pd
import matplotlib.pyplot as plt
from frames import games, info, events

plays = games.query("type=='play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
