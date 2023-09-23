with open('input/day4.txt') as infile:
    lines = infile.read().splitlines()

def assignments_fully_overlap(elve_pair):
    #print(elve_pair)
    section_assignments = [range(int(lower), int(upper)+1)
                for r in elve_pair.split(",")
                    for lower, upper in [r.split('-')]]

    a = set(section_assignments[0])
    b = set(section_assignments[1])

    # Part 1
    #return a.issubset(b) or b.issubset(a)

    # Part 2
    return a & b

# Find overlapping assignments
overlap = [assignments_fully_overlap(l) for l in lines]

# Count pairs with overlap
count_overlapped = len([b for b in overlap if b])
print("Count overlapped:", count_overlapped)
#print("Results", overlap)
