import json
from sportsipy.fb.team import Team
from sportsipy.fb.schedule import Schedule
from sportsipy.fb.roster import Roster

# team ids are in order?
# "Manchester City",
# "Liverpool",
# "Chelsea",
# "Tottenham Hotspur",
# "Arsenal",
# "Manchester United",
# "West Ham United",
# "Wolverhampton Wanderers",
# "Leicester City",
# "Brighton & Hove Albion",
# "Newcastle United",
# "Brentford",
# "Southampton",
# "Crystal Palace",
# "Aston Villa",
# "Leeds United",
# "Everton",
# "Burnley",
# "Watford",
# "Norwich City"

teams = ['Manchester City', "Liverpool", "Chelsea", "Tottenham Hotspur", "Arsenal", "Manchester United", "West Ham United", "Wolverhampton Wanderers", "Leicester City", "Brighton & Hove Albion",
       "Newcastle United", "Brentford", "Southampton", "Crystal Palace", "Aston Villa", "Leeds United", "Everton", "Burnley", "Watford", "Norwich City"]

def metadata(team):
    data = Team(team)
    metadata = {
        "Team Name": data.name,
        "Position": data.position,
        "Record": data.record,
        "Points": data.points,
        "Goals": data.goals_scored,
        "Goals Against": data.goals_against,
    }
    return metadata

def schedule(team):
    team_schedule = Schedule(team)
    schedule = {
        "Games": len(team_schedule)
    }
    return schedule

def roster(team):
    team_roster = Roster(team)
    roster = {
        "Players": len(team_roster)
    }
    return roster

def league_obj(teams):
    pl = {}
    for team in teams:
        pl[team] = {}
        pl[team]["metadata"] = metadata(team)
        pl[team]["schedule"] = schedule(team)
        pl[team]["roster"] = roster(team)
    
    return pl

def main():

    pl = league_obj(teams)

    outfile = open("./premier-league.json", "w")
    pl_json = json.dumps(pl)
    outfile.write(pl_json)
    outfile.close()


if __name__ == "__main__":
    main()
