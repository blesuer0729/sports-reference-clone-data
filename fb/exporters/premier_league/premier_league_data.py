from sportsipy.fb.team import Team
from sportsipy.fb.schedule import Schedule
from sportsipy.fb.roster import Roster

def metadata(team):
    data = Team(team)
    print(data)
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
