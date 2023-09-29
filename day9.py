import os
from math import pow, sqrt, floor
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def len(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalize(self):
        magnitude = self.len()
        return Vector(self.x / magnitude, self.y / magnitude)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def floor(self):
        return Vector(floor(self.x), floor(self.y))

    def __eq__(self, other):
        is_tuple = type(other) is tuple
        x = other[0] if is_tuple else other.x
        y = other[1] if is_tuple else other.y
        return self.x == x and self.y == y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

    def __str__(self):
        return f"Vec({self.x}, {self.y})"

# Visibility controls for debugging
cols = 120
rows = 120
start_pos = Vector(29, 10)  # For the sample scenario: Vector(11, 5)


# The positions of all knots at any given time
knot_count = 10
knots = [start_pos for i in range(knot_count)]

# Store all tail locations
tail_moves = []
last_move = (-1, -1)
# Direction vectors
dir_moves = {
    'U': Vector(0, 1),
    'L': Vector(-1, 0),
    'R': Vector(1, 0),
    'D': Vector(0, -1)
}

with open('input/day9.txt') as infile:
    lines = infile.read().splitlines()

# Debugging helper for matching sample and troubleshooting
def print_table(items):
    keyed = set(items)

    def get_symbol(key):
        show_knot_index = False

        if key == start_pos:
            return "s"
        elif show_knot_index:
            i = items.index(key)
            return "H" if i == 0 else i
        else:
            return "#"

    for row in reversed(range(rows)):
        print(f"{row:2} ", end="")
        for col in range(cols):
            key = (col, row)
            print(get_symbol(key)  if key in keyed else ".", end="" if col < cols -1 else "\n")
            #print("#" if any(s.x == col and s.y == row for s in stops) else "-", end="" if col < cols -1 else "\n")

# Get the change in x/y to move the given node
def get_movement_dir(v):
    x = 0 if v.x == 0 else v.x/abs(v.x)
    y = 0 if v.y == 0 else v.y/abs(v.y)
    return Vector(x, y)

def advance(dir):
    return list(__advance_list(dir))

def __advance_list(dir):
    position = knots[0] + dir_moves[dir]

    # Loop over knots, moving as needed
    for i in range(len(knots)):
        if i > 0:
            diff = position - knots[i]
            position = knots[i] if diff.len() < 2 else knots[i] + get_movement_dir(diff)

        # return
        yield position

# Process move operations from input file
for line in lines:
    #if DBG: print(line)
    dir, count = line.split()
    count = int(count)

    # Perform n moves in the given direction
    for i in range(count):
        knots = advance(dir)
        m = knots[-1]
        if m != last_move:
            last_move = m
            tail_moves.append(m)

    # Per move command debugging
    # os.system('cls')
    # print_table(knots)
    # print()

print("\nTail moves")
print_table([m for m in tail_moves])

print("Total Moves:", len(set(tail_moves)))

