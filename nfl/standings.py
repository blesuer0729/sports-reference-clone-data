import pandas as pd
import json

def generate(db, season):
    dbCollStandings = db["nflStandings"]

    afc = pd.read_html("../input-data/nfl/" + season + "/Afc.xls")
    nfc = pd.read_html("../input-data/nfl/" + season + "/Nfc.xls")
    afc_df = afc[0]
    nfc_df = nfc[0]
    nfl_standings_dict = {
        "season": season,
        "afc": {},
        "nfc": {}
    }

    for i in range(0,16):
        team = afc_df.loc[i]
        nfl_standings_dict["afc"][team['Tm']] = {
            "wins": int(team['W']),
            "losses": int(team['L']),
            "ties": int(team['T']),
            "win %": team['W-L%'],
            "points for": int(team['PF']),
            "points against": int(team['PA']),
            "differential": int(team['PD']),
        }

    for x in range(0,16):
        team = nfc_df.loc[x]
        nfl_standings_dict["nfc"][team['Tm']] = {
            "wins": int(team['W']),
            "losses": int(team['L']),
            "ties": int(team['T']),
            "win %": team['W-L%'],
            "points for": int(team['PF']),
            "points against": int(team['PA']),
            "differential": int(team['PD']),
        }

    # output is going to be handled by pymongo
    output = nfl_standings_dict
    runInsert = dbCollStandings.insert_one(nfl_standings_dict)
