# For each elve, take a string with their current values and return
# the sum of those values
def extractAndSumCounts(s):
    counts = [int(n) for n in s.splitlines()]
    return sum(counts)

# Build two arrays from the input file
with open("input/day1.txt") as f:
    # Create a string for each elve that contains its counts
    elves  = f.read().split("\n\n")

    # Convert those counts into a sum
    elveTotals = [extractAndSumCounts(e) for e in elves]

# Sort in reverse order by summed value
sorted_elves = sorted(elveTotals, reverse=True)

# Print the largest value
print(sorted_elves[0])



print(sum(sorted_elves[0:3]))