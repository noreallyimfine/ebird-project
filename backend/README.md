# Back-End
Repository for database and back end api code

## Endpoints
```
Endpoint: /api/birds

Method: GET

Response: {'birds': <List of birds>}
```


```
Endpoint: /api/seasons

Method: GET

Response: {'seasons': ['Summer', 'Winter', 'Fall', 'Spring']}
```

```
Endpoint: /api/states

Method: GET

Response: {'states': <List of states>}
```

```
Endpoint: /api/counties

Method: POST

Arguments: {'state': <state>}

Response: {'counties': <List of counties in the state>}
```

```
Endpoint: /api/results

Method: POST

Arguments: {
    "bird": <bird>,
    "season": <season>,
    "state": <state>,
    "county: <county>
}

Response: {"result": <One of ('Common', 'Uncommon', 'Rare')>}
```
