file_path = r'input/day1.txt'

calorie_list = []
calorie_sums = []
dummy_value = -5
sub_total = 0

# Open raw data and read lines into list.
# Change strings into integers and replace empty lines with dummy value for sorting


# Read the file and split into an array of groups - identified by an empty line
with open(file_path) as f:
    groups = f.read().split('\n\n')
    print(groups[0:5])


def getTotals(group):
    # Split into an array with calorie counts
    counts = [int(n) for n in group.splitlines()]

    # Return the sum
    return sum(counts)

# Compute totals for each group
totals = list(map(getTotals, groups))
print(totals[0:10])


sorted_totals = sorted(totals)[::-1]
print(sorted_totals[0:10])

top_3 = sorted_totals[0:3]

print(f"Top calorie load is : {sorted_totals[0]}")
print(f"Sum of top 3 carriers is: {sum(top_3)}")

Top calorie load is : 67791
Sum of top 3 carriers is: 207968