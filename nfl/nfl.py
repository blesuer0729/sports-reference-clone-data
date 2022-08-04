import argparse
import standings
import schedule
from pymongo import MongoClient

# DB config
dbclient = MongoClient("mongodb://admin:password@localhost:27017/")
db = dbclient["sportsref"]
standingsColl = db["Standings"]
schedulesColl = db["Schedules"]

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
            standingsObj = standings.generate(season)
            runInsert = standingsColl.insert_one(standingsObj)
            for team in teams:
                scheduleObj = schedule.generate(season, "Cowboys")
                runInsert = schedulesColl.insert_one(scheduleObj)
    else:
        standingsObj = standings.generate(args.season)
        runInsert = standingsColl.insert_one(standingsObj)
        for team in teams:
            print('putting team ' + team)
            scheduleObj = schedule.generate(args.season, "Cowboys")
            runInsert = schedulesColl.insert_one(scheduleObj)

if __name__ == "__main__":
    main()