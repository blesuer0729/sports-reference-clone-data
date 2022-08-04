import argparse
import standings
import schedule
from pymongo import MongoClient

# DB config
dbclient = MongoClient("mongodb://admin:password@localhost:27017/")
db = dbclient["sportsref"]

# args config
parser = argparse.ArgumentParser()
parser.add_argument("--season", type=str, help="Set this flag to all or a specific season you want to import data for")
args = parser.parse_args()

seasons = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]
teams = ["Bills", "Patriots", "Dolphins", "Jets", "Bengals", "Steelers", "Browns", "Ravens", "Titans", "Colts", "Texans", "Jaguars", "Chiefs", "Raiders", "Chargers", "Broncos",
        "Cowboys", "Eagles", "Commanders", "Giants", "Packers", "Vikings", "Bears", "Lions", "Buccaneers", "Saints", "Falcons", "Panthers", "Rams", "Cardinals", "49ers", "Seahawks"]

def main():
    if (args.season == 'all'):
        for season in seasons:
            standings.generate(db, season)
            for team in teams:
                schedule.generate(db, season, team)
    else:
        standings.generate(db, args.season)
        for team in teams:
            schedule.generate(db, args.season, team)

if __name__ == "__main__":
    main()