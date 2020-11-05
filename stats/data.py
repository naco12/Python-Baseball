import os # allow to work with a collection of files
import glob # allow to work with a collection of files
import pandas as pd

#files managements
# game_files contains a list of file names that end with .EVE in the games folder
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# sorting files in game_files to prepare for pandas use
game_files.sort()

game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names =  ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)
    #concatenate Dataframes
    games = pd.concat(game_frames)

# dataframe Cleaning. replacing ?? in column multi5 with ''
games.loc[games['multi5']== '??', ['multi5']] = ''

#Extract Identifiers. Each row of data should be associated with the proper game id
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

#ffill: propagate last valid observation forward to next valid backfill
identifiers = identifiers.fillna(method='ffill')

#renaming identifiers dataframe columns nAmateur
identifiers.columns = ['game_id', 'year']

#Concatenate identifier Columns
games = pd.concat([games, identifiers], axis=1, sort=False)

games = games.fillna('')

games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

games.head()
