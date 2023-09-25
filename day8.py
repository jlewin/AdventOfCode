
with open('input/day8.txt') as infile:
    lines = infile.read().splitlines()

trees = [list(l) for l in lines]
visible_trees = []

rows = len(trees)
cols = len(trees[0])

# Loop over rows and columns
for r in range(rows):
    for c in range(cols):
        # Select row and column from list
        row = trees[r]
        col = [trees[i][c] for i in range(rows)]

        # This tree's height
        height = row[c]

        next_column = c + 1
        next_row = r + 1

        # Get lists for up/left/right/down siblings
        up = col[0:r]
        left = row[0:c]
        right = row[next_column:]
        down = col[next_row:]

        # Push visibility results into tuple for improved debugging
        visibility = [
            ('up', len(up) == 0 or height > max(up)),
            ('left', len(left) == 0 or height > max(left)),
            ('right', len(right) == 0  or height > max(right)),
            ('down', len(down) == 0 or height > max(down))]

        # Consider all four direcions for tree visibility
        is_visible = any([v[1] for v in visibility])
        visible_trees.append(is_visible)

        # Debugging helper
        #print(f"({r}, {c})", "\tVisible", is_visible, visibility)

# Print results
print("Visible trees", sum(visible_trees))

