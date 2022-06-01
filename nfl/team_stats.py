import pandas as pd
import json

teams = ["dallas"]

def parse_stats(team):
    stats = pd.read_html("./input/teams/"+team+"/stat_rankings.xls")
    stats_df = stats[0]

    team_obj = {
        "season": 2021,
        "Total Offense": {},
        "Passing": {},
        "Rushing": {},
        "Average Drive": {},
    }

    total_offense = stats_df.loc[:, "Tot Yds & TO"]
    passing = stats_df.loc[:, "Passing"]
    rushing = stats_df.loc[:, "Rushing"]
    penalties = stats_df.loc[:, "Penalties"]
    average_drive = stats_df.loc[:, "Average Drive"]

    outfile = open("./output/teams/"+team+"/stat_rankings.json", "w")
    output = json.dumps(team_obj)
    outfile.write(output)
    outfile.close()

    

def parse_schedule(team):
    schedule = pd.read_html("./input/teams/"+team+"/schedule.xls")
    schedule_df = schedule[0]

    team_obj = {
        "season": 2021,
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

    game = schedule_df.loc[:, "Game"]
    score = schedule_df.loc[:, "Score"]
    offense = schedule_df.loc[:, "Offense"]
    defense = schedule_df.loc[:, "Defense"]
    expected_points = schedule_df.loc[:, "Expected Points"]


    outfile = open("./output/teams/"+team+"/schedule.json", "w")
    output = json.dumps(team_obj)
    outfile.write(output)
    outfile.close()

for team in teams:
    parse_stats(team)
    parse_schedule(team)



