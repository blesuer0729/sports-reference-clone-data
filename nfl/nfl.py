import argparse
import standings
import schedule

parser = argparse.ArgumentParser()
parser.add_argument("--season", type=str, help="Set this flag to all or a specific season you want to import data for")
args = parser.parse_args()

seasons = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]
teams = ["Bills", "Patriots", "Dolphins", "Jets", "Bengals", "Steelers", "Browns", "Ravens", "Titans", "Colts", "Texans", "Jaguars", "Chiefs", "Raiders", "Chargers", "Broncos",
        "Cowboys", "Eagles", "Commanders", "Giants", "Packers", "Vikings", "Bears", "Lions", "Buccaneers", "Saints", "Falcons", "Panthers", "Rams", "Cardinals", "49ers", "Seahawks"]

def main():
    if (args.season == 'all'):
        for season in seasons:
            standings.generate(season)
            for team in teams:
                schedule.generate(season, team)
    else:
        standings.generate(args.season)
        for team in teams:
            schedule.generate(args.season, team)

if __name__ == "__main__":
    main()