import pandas as pd
import json

def generate(db, season, team):
    dbCollTeam = db["nfl" + team]

    # schedule = pd.read_html("../input-data/nfl/" + season + "/" + team + ".xls")
    # schedule_df = schedule[0]

    nfl_team_dict = {
        "season": season,
        "team": team,
        "Week 1": {},
        "Week 2": {},
        "Week 3": {},
        "Week 4": {},
        "Week 5": {},
        "Week 6": {},
        "Week 7": {},
        "Week 8": {},
        "Week 9": {},
        "Week 10": {},
        "Week 11": {},
        "Week 12": {},
        "Week 13": {},
        "Week 14": {},
        "Week 15": {},
        "Week 16": {},
        "Week 17": {},
        "Week 18": {},
    }

    # game = schedule_df.loc[:, "Game"]
    # score = schedule_df.loc[:, "Score"]
    # offense = schedule_df.loc[:, "Offense"]
    # defense = schedule_df.loc[:, "Defense"]
    # expected_points = schedule_df.loc[:, "Expected Points"]

    # output is going to be handled by pymongo
    output = nfl_team_dict
    runInsert = dbCollTeam.insert_one(nfl_team_dict)