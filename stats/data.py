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

# dataframe Cleaning
games.loc[[games[multi5]=='??'], [multi5]] = ''
