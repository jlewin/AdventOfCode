
with open('input/day7.txt') as infile:
    lines = infile.read().splitlines()

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size} b"

class Node:
    def __init__(self, name, parent=None):
        self.children = []
        self.files = []
        self.name = name
        self.parent = parent

    @property
    def data(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def dump(self):
        print(self.name, self.get_size(), "b", [str(f) for f in self.files])

    def add_file(self, name, size):
        self.files.append(File(name, int(size)))

    def get_size(self):
        # Walk all descendants, summing their size and ours
        return sum([f.size for f in self.files]) + sum([d.get_size() for d in self.children])

    def __str__(self):
        return f"{self.name} (Parent: {self.parent.name if self.parent else ''}) {self.get_size()} b"

current_dir = Node("root")
root = current_dir
all_dirs = []
stack = []

for line in lines:
    print(line)
    if line.startswith("$ cd"):
        directory = line[5:]

        # cd either pushes or pops the stack
        if directory == "..":
            current_dir = current_dir.parent
            stack.pop()
            print("Changing to", current_dir)

        else:
            print("Parent", current_dir, "Child", directory)
            sub = Node(directory, current_dir)
            current_dir.add_child(sub)
            current_dir = sub
            all_dirs.append(current_dir)
            stack.append(current_dir)

    elif line.startswith("$ ls"):
        listing_results = True
    elif listing_results:
        size, name = line.split()
        if size != "dir":
            current_dir.add_file(name, size)
            current_dir.dump()

    if line.startswith("&") and listing_results:
        listing_results = False

"""
# Part 1
max_size = 100000
filtered = [d.get_size() for d in all_dirs if d.get_size() < max_size]
#print(filtered)
print(f"Sum of directories less than {max_size}: {sum(filtered)}")
"""

# Part 2
disk_size = 70000000
min_required = 30000000

used_bytes = root.get_size()
free_bytes = disk_size - used_bytes
min_delete =  min_required - free_bytes

# Find the directories which are at least the minimum del size required
targets = [d for d in all_dirs if d.get_size() >= min_delete]

# Sort by size
targets.sort(key=lambda d: d.get_size())
#print([str(d) for d in targets])

# Take the smallest
print("Target to delete", targets[0].name, targets[0].get_size())
