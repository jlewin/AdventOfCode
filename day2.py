file_path = r'input/day2.txt'

# Read the file and split into an array of groups - identified by an empty line
with open(file_path) as f:
    plays = f.read().splitlines()

rock = 1
paper = 2
scissors = 3

win = 6
draw = 3
lose = 0

# Mapping from known ids to score

# Maps what to play for a given lose/win goal
#   They play rock, you lose with paper, win with 
rules = {
    rock: {
        'id': 'R',
        'ids': 'RAX',
        'score': 1,
        win: paper,
        lose: scissors,
    },
    paper: {
        'id': 'P',
        'ids': 'PBY',
        'score': 2,
        win: scissors,
        lose: rock
    },
    scissors: {
        'id': 'S',
        'ids': 'SCZ',
        'score': 3,
        win: rock,
        lose: paper
    }
}

# Map all symbols to their numeric constant
symbolToRule = {chr:rule for (k, rule) in rules.items() for chr in rule['ids'] }
#print(symbolToRule)

def executeRound(moves):
    # Remap the unique symbols to their numeric constants
    elveMove, outcome  = [symbolToRule[m]['score'] for m in moves.split(' ')]

    if (outcome == 1 ):   # X/lose
        goal = lose
    elif (outcome == 2 ): # Y/draw
        goal = draw
    else:                 # Z/win
        goal = win

    # Find the win/lose move for the given target outcome
    myMove = elveMove if goal == draw else rules[elveMove][goal]

    # The amount you score is simply the constant value of the move
    moveScore = myMove

    if elveMove == myMove:
        winnings = draw
    elif elveMove == rock:      # Win: R < P
        winnings = win if myMove == paper else lose
    elif elveMove == paper:     # Win: P < S
        winnings = win if myMove == scissors else lose
    elif elveMove == scissors:  # Win: S < R
        winnings = win if myMove == rock else lose

    return winnings + moveScore

# Process all rounds into scores
scores = [executeRound(play) for play in plays]

# Dump
print("Total score:", sum(scores))
