import string

input_data = r'input/day4.txt'

rucksacks0 = []

# with open(input_data) as my_file:
#     contents = my_file.read().splitlines()
#     for n in contents:
#         rucksacks.append(n)

def remapToPriority(c):
    pos = ord(c)
    return pos - (96 if ord('a') <= pos <= ord('z') else 38)

rucksacks0 = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw" ]

# Split the rucksacks into their compartment values (split at midpoint)
rucksacks1 = [(s[:mid], s[mid:]) for s in rucksacks0 for mid in [int(len(s) / 2)]]
#print(rucksacks1)

# Intersect the two strings to find matching characters between them
rucksacks2 = [set(c1) & set(c2) for (c1, c2) in rucksacks1]
#print(rucksacks2)

# Remap the intersected characters to their prioritys
rucksacks3 = [remapToPriority(c) for s in rucksacks2 for c in s ]
#print(rucksacks3)

# Sum the priorities
print(sum(rucksacks3))



# strings = ['hello', 'world22']
# modified = [s_mod for s in strings for s_mod in [len(s)]]
# print(modified) 