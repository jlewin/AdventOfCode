with open('input/day5.txt') as infile:
    text = infile.read()

crate_lines, moves = [t.splitlines() for t in text.split('\n\n')]
crate_lines.reverse()

def split_by(n, line):
    return [ line[i:i+n].strip() for i in range(0, len(line), n)]

stacks = [split_by(4, line) for line in crate_lines]

# Transposing 2D list, drop empty values
stacks = [[row[i] for row in stacks if len(row[i])] for i in range(len(stacks[0]))]
#print(stacks)

def dump():
    row_count = max([len(stacks[c]) for c in range(0, 9)])

    for r in range(row_count):
        for c in range(9):
            stack = stacks[c]

            if r == 0:
                print("", stack[r], " ", end='')
            elif len(stack) > r:
                print(stack[r] + " ", end='')
            else:
                print("    ", end='')
        print('')

    print()

dump()

# Execute all moves (move <c> from <f> to <t>)
for line in moves:
    # Extract operations
    segments = line.split()
    count = int(segments[1])
    move_from = int(segments[3]) - 1
    move_to = int(segments[5]) - 1

    # Move n crates from -> to
    removed_crates = [stacks[move_from].pop() for x in range(count)]
    removed_crates.reverse()
    stacks[move_to].extend(removed_crates)

    #print(line)
    #dump()

#dump()
print()
# Print items on the top of the stacks
for c in range(0, 9):
    stack = stacks[c]
    print(stack[-1].removeprefix("[").removesuffix("]"), end='')
print()