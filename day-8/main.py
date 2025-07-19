# --- Day 8: Resonant Collinearity ---
import itertools
import pprint

with open("day-8/input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

height = len(grid)
width = len(grid[0])
result_antinodes = ["." * height for _ in range(width)]
pprint.pprint(result_antinodes)

antennas = {}

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != ".":
            if grid[row][col] not in antennas.keys():
                antennas[grid[row][col]] = [(row, col)]
            else:
                antennas[grid[row][col]].append((row, col))

print(antennas)

total = set()

for freq, antenna_list in antennas.items():
    if len(antenna_list) < 2:
        continue

    for antenna1, antenna2 in itertools.combinations(antenna_list, r=2):
        y_distance = antenna2[0] - antenna1[0]
        x_distance = antenna2[1] - antenna1[1]
        
        lower_antinode = (antenna2[0] + (y_distance)), (antenna2[1] + (x_distance))
        upper_antinode = (antenna1[0] - (y_distance)), (antenna1[1] - (x_distance))

        if upper_antinode[0] >= 0 and upper_antinode[0] < height:
            if upper_antinode[1] >= 0 and upper_antinode[1] < width:
                text = result_antinodes[upper_antinode[0]]
                result_antinodes[upper_antinode[0]] = text[:upper_antinode[1]] + "#" + text[upper_antinode[1]+1:]
                total.add(upper_antinode)
        if lower_antinode[0] >= 0 and lower_antinode[0] < height:
            if lower_antinode[1] >= 0 and lower_antinode[1] < width:
                text = result_antinodes[lower_antinode[0]]
                result_antinodes[lower_antinode[0]] = text[:lower_antinode[1]] + "#" + text[lower_antinode[1]+1:]
                total.add(lower_antinode)

pprint.pprint(result_antinodes)
print(len(total))
