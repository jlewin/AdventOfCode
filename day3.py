import string

input_data = r'input/day3.txt'

rucksacks = []

with open(input_data) as my_file:
    contents = my_file.read().splitlines()
    for n in contents:
        rucksacks.append(n)

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
values = []
for x in range(1, 53):
    values.append(x)

translation = {priorities: values for priorities, values in zip(priorities, values)}
groups_of_3 = []
group = []

# Put into groups of 3
for x in range(0, len(rucksacks)):
    # Group in intervals of 3
    if x % 3 == 0:
        # Append group
        groups_of_3.append(group)
        group = [rucksacks[x]]
    else:
        group.append(rucksacks[x])

# Append final group
if group not in groups_of_3:
    groups_of_3.append(group)

no_dupes = []

# remove duplicates from each elf pack

for badges in groups_of_3:
    for line in badges:
        a = sorted(set(line))
        no_dupes.append(a)

# put sets back in groups of 3
sub_total = []
final = []

for x in range(0, len(rucksacks)):
    if x % 3 == 0 and x != 0:
        # Append group
        final.append(sub_total)
        sub_total = [no_dupes[x]]
    else:
        sub_total.append(no_dupes[x])

# Append final group
if sub_total not in final:
    final.append(sub_total)


print(final)
badges = []
for x in range(0, 1):
    for item in final:
        for c in item[x]:
            for char in c:
                if char in item[0] and char in item[1] and char in item[2]:
                    badges.append(char)

print(badges)
# print(rucksacks[-1])
# print(groups_of_3[-1])
# print(no_dupes[-1])
# print(final[-1])
# print(final[-1][-1])
sum_of_badges = []
for val in badges:
    x = translation.get(val)
    sum_of_badges.append(x)
# print(f" Rucksacks : {len(rucksacks)}")
# print(f" Groups of 3 : {len(groups_of_3)}")
# print(f" No_dupes: {len(no_dupes)}")
# print(f" Final: {len(final)}")

print(sum_of_badges)
print(sum(sum_of_badges))