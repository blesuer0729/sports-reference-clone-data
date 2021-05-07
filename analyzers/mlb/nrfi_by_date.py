from sportsipy.mlb.boxscore import Boxscores, Boxscore
from datetime import datetime, date
import argparse
import math

# argparse library for getting page range
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=str, help="The first date in the date range")
parser.add_argument("--stop", type=str, help="The final date in the date range")
args = parser.parse_args()

# Used to get a range of games from API
start_date = datetime.strptime(args.start, "%m-%d-%Y")
end_date = datetime.strptime(args.stop, "%m-%d-%Y")

# Given a date, get all boxscores for that day
# and determine how many NRFI there were
games_range = Boxscores(start_date, end_date)
for x in range(0,len(games_range.games)):
    game_date = list(games_range.games)[x]
    game_dict = games_range.games[game_date]
    total_nrfi = 0
    for x in range(0,len(game_dict)):
        game_boxscore = Boxscore(game_dict[x]['boxscore'])
        if(game_boxscore.summary['away'][0] == 0 and game_boxscore.summary['home'][0] == 0):
            total_nrfi+=1
    # result
    print("% of NRFI games on " + str(game_date) + ": " + str(total_nrfi) + "/" + str(len(game_dict)) + " = " + str(math.floor((total_nrfi / len(game_dict)) * 100)) + "%")