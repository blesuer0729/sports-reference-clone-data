# sports-reference to JSON

In order to create a clone front-end for sports-reference.com I needed something to pull the data from.

After downloading all of the nesecarry tables off sports-reference this project allows you to bootstrap a MongoDB with all the necessary data to populate the front-end.

## Pre requisites

A running mongoDB instance that you can connect to and an environment variable for the connection uri

- e.g. MONGO_URI="mongodb://localhost:27017/"

## Data

Included data for the following sports for the last 5 seasons

- NFL
  - AFC / NFC Standings data
  - Team Schedule data

- NBA

- NHL

- MLB

## Running

NFL
To run the script and generate the included nfl input data in your db for a given season:

```bash
python3 nfl.py --season 2021
```

the ```--season``` flag is required and can either be ```all``` or a year e.g. ```2021```
