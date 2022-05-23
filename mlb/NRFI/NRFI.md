# getting MLB - NRFI data as JSON

A No Run First Inning (NRFI) is a statistic where in a game the score was 0-0 after the first inning. You may want this info for example if you were going to place a wager on a game whether there will be a NRFI or not.

## NRFI by date range

```bash
python3 nrfi_by_date.py --start 01-01-2022 --stop 01-05-2022
```

## NRFI by team

```bash
python3 nrfi_by_team.py --team WSN --detailed:OPTIONAL
```
