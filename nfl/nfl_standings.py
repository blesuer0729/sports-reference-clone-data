import pandas as pd
import json

afc = pd.read_html("./input/AFC.xls")
nfc = pd.read_html("./input/NFC.xls")
afc_df = afc[0]
nfc_df = nfc[0]
nfl_standings = {
    "afc": {},
    "nfc": {}
}

# print(afc_df)
# print(nfc_df)

i = 0
while i < len(afc_df):
    team = afc_df.loc[i]
    nfl_standings["afc"][team['Tm']] = {
        "wins": int(team['W']),
        "losses": int(team['L']),
        "ties": int(team['T']),
        "win %": int(team['W-L%']),
        "points for": int(team['PF']),
        "points against": int(team['PA']),
        "differential": int(team['PD']),
    }
    i += 1

x = 0
while x < len(nfc_df):
    team = nfc_df.loc[x]
    nfl_standings["nfc"][team['Tm']] = {
        "wins": int(team['W']),
        "losses": int(team['L']),
        "ties": int(team['T']),
        "win %": int(team['W-L%']),
        "points for": int(team['PF']),
        "points against": int(team['PA']),
        "differential": int(team['PD']),
    }
    x += 1

outfile = open("./output/nfl_standings.json", "w")
output = json.dumps(nfl_standings)
outfile.write(output)
outfile.close()
