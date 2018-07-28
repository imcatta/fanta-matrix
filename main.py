import sys 


TEAMS = {
    'T1': 1,
    'T2': 1,
    'T3': 1,
    'T4': 1,
    'T5': 1,
    'T6': 7,
     }

MATCHES = (
    (('T1', 'T2'), ('T3', 'T4'), ('T5', 'T6'),),
    (('T1', 'T3'), ('T4', 'T5'), ('T2', 'T6'),),
    (('T1', 'T4'), ('T2', 'T5'), ('T3', 'T6'),),
    (('T1', 'T5'), ('T2', 'T3'), ('T4', 'T6'),),
    (('T1', 'T6'), ('T2', 'T4'), ('T3', 'T5'),),
)


def _find_match(team, week):
    return next(x for x in MATCHES[week] if team in x)

def _opponent(team, match):
    return match[1] if match[0] == team else match[0]

def _match_difficult(team, match):
    opponent = _opponent(team, match)
    return TEAMS[opponent] - TEAMS[team]

def calculate_difficult(teams):
    difficult = 0
    for week in range(len(MATCHES)):
        week_difficult = float('Inf')
        for team_name in teams:
            match = _find_match(team_name, week)
            week_difficult = min(_match_difficult(team_name, match), week_difficult)
        difficult += week_difficult
    
    return difficult


def main():
    print(calculate_difficult(sys.argv[1:]))           


if __name__ == '__main__':
    main()