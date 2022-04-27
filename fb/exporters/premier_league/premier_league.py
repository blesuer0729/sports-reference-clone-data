import premier_league_data
import json

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

teams = ['b8fd03ef', 'e87167c6', 'a6a4e67d', '361ca564', '411b1108', '19538871', '52d65cea', '8cec06e1', 'a2d435b3', 'd07537b9',
       'b2b47a98', 'cd051869', '33c895d4', '47c64c55', '8602292d', '5bfb9659', 'c4989550', '943e8050', '2abfe087', '1c781004']


def main():

    pl = premier_league_data.league_obj(teams)

    outfile = open("fb/exporters/output/premier_league.json", "w")
    pl_json = json.dumps(pl)
    outfile.write(pl_json)
    outfile.close()


if __name__ == "__main__":
    main()
