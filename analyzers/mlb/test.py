from sportsipy.mlb.teams import Teams
from sportsipy.mlb.schedule import Schedule

nats_schedule = Schedule('WSN')

for game in nats_schedule:
    print(game.result)