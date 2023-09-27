from math import pow, sqrt, floor

# Toggle for debugging
DBG = False

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vec({self.x}, {self.y})"

    def len(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

with open('input/day9.txt') as infile:
    lines = infile.read().splitlines()

x = y = 0
cols = rows = 0
stops = [] # Tail stops
head = Vector(0, 0)
tail = Vector(0, 0)

# Direction vectors
moves = {
    'U': Vector(0, 1),
    'L': Vector(-1, 0),
    'R': Vector(1, 0),
    'D': Vector(0, -1)
}

# Loop over moves
for line in lines:
    if DBG: print(line)
    dir, count = line.split()
    count = int(count)

    # Perform n moves
    for i in range(count):
        start_pos = head
        head = head + moves[dir]
        length = (head - tail).len()
        if length >= 2:
            tail = start_pos
            stops.append(tail)
            if DBG: print("Moving: ", head, tail, length)

print("Total Moves:", len(set(stops)))

# Debugging 
if DBG:
    def print_table():
        cols = 6
        rows = 5
        stops.sort(key=lambda v: v.y)
        #grr = [str(s) for s in stops]

        for j in range(30):
            col = j % cols
            row = floor(j / cols)
            #print (row, col)

            print("#" if any(s.x == col and s.y == row for s in stops) else "-", end="" if col < cols -1 else "\n")

    print_table()
