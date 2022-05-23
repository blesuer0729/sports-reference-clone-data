# getting premier league data as JSON

The premier league stats on fb-reference have no option to export tables in JSON format.

## running

```bash
python3 premier-league.py
```

## output format

```json
{
    team: {
        metadata: {},
        schedule: {},
        roster: {},
    },
    team...,
    team...,
}
```
