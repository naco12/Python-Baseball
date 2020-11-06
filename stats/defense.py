import pandas as pd
import matplotlib.pyplot as plt
from frames import games, info, events

plays = games.query('games['type']=='play' & games['event']!='NP'')
