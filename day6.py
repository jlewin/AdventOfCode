i = 0
marker_size = 14 # {part1: 4, part2: 14}

f = open('input/day6.txt')

while True:
    marker = f.read(marker_size)

    # If no duplicate character, marker found
    if len(set(marker)) == marker_size:
        print("Marker:", marker, "Marker End: ", i + marker_size)
        break

    #print(i, marker)

    # Rewind the stream to the next character
    i = i + 1
    f.seek(i)
