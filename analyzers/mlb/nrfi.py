from sportsipy.mlb.boxscore import Boxscores, Boxscore
from datetime import datetime, date

# Used to get todays games from API
start_date = datetime(2021, 4, 25)
end_date = datetime(2021, 4, 30)

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
    print("# of NRFI in " + str(game_date) + " games: " + str(total_nrfi) + "/" + str(len(game_dict)) + " = " + str((total_nrfi / len(game_dict)) * 100) + " %")