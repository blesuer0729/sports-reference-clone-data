from sportsipy.mlb.teams import Team
import argparse
import math

# argparse library for getting page range
parser = argparse.ArgumentParser()
parser.add_argument("--team", type=str, help="The team abbreviation (ex: WSN is Washington Nationals) used to gather nrfi data")
parser.add_argument("--detailed", action='store_true', help="If run with --detailed every played game will be printed along with whether it was NRFI or not")
args = parser.parse_args()

# beginning variables used in final output
team = Team(args.team)
team_schedule = team.schedule
nrfi_yes = 0
nrfi_no = 0
games_played = 0

# given a team find the percentage of NRFI from games they have played so far this season
for game in team_schedule:
    if(game.boxscore.summary != None):
        if(game.boxscore.summary['away'][0] == 0 and game.boxscore.summary['home'][0] == 0):
            nrfi_yes+=1
            games_played+=1
            if(args.detailed):
                print(str(game.boxscore) + " NRFI - YES")
        else:
            nrfi_no+=1
            games_played+=1
            if(args.detailed):
                print(str(game.boxscore) + " NRFI - NO")
    else:
        break
print(str(team.name) + " NRFI % for games played this season: " + str(nrfi_yes) + "/" + str(games_played) + " = " + str(math.floor((nrfi_yes / games_played) * 100)) + "%")
