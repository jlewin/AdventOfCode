from itertools import takewhile

with open('input/day8.txt') as infile:
    lines = infile.read().splitlines()

# Covert each line into list of ints, in a list of lists
trees = [[int(char) for char in l] for l in lines]
rows = len(trees)
cols = len(trees[0])

max_score = 0

# Loop over rows and columns
for r in range(rows):
    for c in range(cols):
        # Select row and column from list
        row = trees[r]
        col = [trees[i][c] for i in range(rows)]

        height = row[c]  # This tree's height
        next_column = c + 1
        next_row = r + 1

        # Get lists for up/left/right/down siblings
        up = col[0:r]
        left = row[0:c]
        right = row[next_column:]
        down = col[next_row:]

        # Part 2
        def visible_trees_distance(items):
            visible = []
            distance = 0
            # Loop over the list items, collecting until threshold is hit
            for h in items:
                distance = distance + 1
                visible.append((distance, h))
                if h >= height:
                    break;
            return distance

            #result =  list(takewhile(lambda sibling_height: sibling_height < height, rev))

        # up, left, right, down
        scores = [
            visible_trees_distance(reversed(up)),
            visible_trees_distance(reversed(left)),
            visible_trees_distance(right),
            visible_trees_distance(down),
        ]

        scenic_score = scores[0] * scores[1] * scores[2] * scores[3]
        max_score = max(max_score, scenic_score)

print("Maximum score", max_score)

def part1():
    # Push visibility results into tuple for improved debugging
    visibility = [
        ('up', len(up) == 0 or height > max(up)),
        ('left', len(left) == 0 or height > max(left)),
        ('right', len(right) == 0  or height > max(right)),
        ('down', len(down) == 0 or height > max(down))]

    # Consider all four directions for tree visibility
    is_visible = any([v[1] for v in visibility])
    visible_trees_distance.append(is_visible)

    # Debugging helper
    print(f"({r}, {c})", "\tVisible", is_visible, visibility)



