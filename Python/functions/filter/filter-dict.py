matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

new_list = list(filter(lambda x: x['home_team_result'] == 'Win', matches))
print(matches)
print('lambda', new_list)


def winner_teams(match):
    new_match = match.copy()
    if new_match['home_team_result'] == 'Win':
        return new_match['home_team']


winner_teams_list = list(filter(winner_teams, matches))
print('def', winner_teams_list)
