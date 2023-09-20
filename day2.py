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
rules = {
    'RAX': 1, 
    'PBY': 2, 
    'SCZ': 3 
}

# Maps what to play for a given lose/win goal
#   They play rock, you lose with paper, win with 
play_map = {
    rock: {
        win: paper,
        lose: scissors
    },
    paper: {
        win: scissors,
        lose: rock
    },
    scissors: {
        win: rock,
        lose: paper
    }
}

# Map all symbols to their numeric constant
mappings = {c:r for (k, r) in rules.items() for c in k }
print(mappings)

def executeRound(moves):
    # Remap the unique symbols to their numeric constants
    elveMove, outcome  = [mappings[m] for m in moves.split(' ')]

    if (outcome == 1 ):   # X/lose
        goal = lose
    elif (outcome == 2 ): # Y/draw
        goal = draw
    else:                 # Z/win
        goal = win

    # Find the win/lose move for the given target outcome
    myMove = elveMove if goal == draw else play_map[elveMove][goal]

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


# debugging
#print(scores, "\n", sum(scores))
# #plays = plays[0:5]
# #plays = ["C Y"]

# scores = [executeRound(play) for play in plays]


# # test = """A Y
# # B X
# # C Z"""

# # scores = [executeRound(l) for l in test.splitlines()]

# plays2 = [p.replace('A', 'R').replace('B', 'P').replace('C', 'S')
#           .replace('X', 'R').replace('Y', 'P').replace('Z', 'S') for p in plays]


# print(plays, "\n", plays2, "\n", scores, "\n", sum(scores))

# executeRound("C Y")

