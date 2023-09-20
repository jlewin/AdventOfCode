import string

input_data = r'input/day4.txt'

with open(input_data) as my_file:
    rucksacks = my_file.read().splitlines()

# Remap from ordinal indexes in the character set to the target offsets
def remapToPriority(c):
    pos = ord(c)
    return pos - (96 if ord('a') <= pos <= ord('z') else 38)

# Split the rucksacks into their compartment values (split at midpoint)
compartments = [(s[:mid], s[mid:]) for s in rucksacks for mid in [int(len(s) / 2)]]
#print(compartments)

# Intersect the two strings to find matching items between them
shared_item_types = [set(c1) & set(c2) for (c1, c2) in compartments]
#print(shared_item_types)

# Remap the intersected characters to their priorities
item_priorities = [remapToPriority(c) for s in shared_item_types for c in s ]
#print(item_priorities)

# Sum the item priorities
print("Sum of item priorities:", sum(item_priorities))

# Find badges in each 3 Elven group
badges = []
for i in range(0, len(rucksacks), 3):
    matched = set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])
    assert (len(matched) == 1, 'x must be positive')
    badges.append(list(matched)[0])
#print(badges)

badge_priorities = [remapToPriority(b) for b in badges]
#print(badge_priorities)

# Sum the badge priorities
print("Sum of badge priorites:", sum(badge_priorities))
