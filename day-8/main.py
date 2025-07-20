# --- Day 8: Resonant Collinearity ---
import itertools
import pprint

with open("day-8/input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

HEIGHT = len(grid)
WIDTH = len(grid[0])
result_antinodes = ["." * HEIGHT for _ in range(WIDTH)]
# pprint.pprint(result_antinodes)

antennas = {}

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != ".":
            if grid[row][col] not in antennas.keys():
                antennas[grid[row][col]] = [[row, col]]
            else:
                antennas[grid[row][col]].append([row, col])

print(antennas)

def update_map(point: tuple[int]) -> None:
    text = result_antinodes[point[0]]
    result_antinodes[point[0]] = text[: point[1]] + "#" + text[point[1] + 1 :]


def distance_between_antennas(upper: list[int], lower: list[int]) -> list[int]:
    "Returns the distance between 2 antennas."
    row_distance = lower[0] - upper[0]
    col_distance = lower[1] - upper[1]
    return (row_distance, col_distance)


def in_range(antennas: list[list[int]], distance: list[int], repeat: int = 1):
    antenna1 = antennas[0]
    antenna2 = antennas[1]

    upper_boundaries = (antenna1[0] - (repeat * distance[0])), (
        antenna1[1] - (repeat * distance[1])
    )
    lower_boundaries = (antenna2[0] + (repeat * distance[0])), (
        antenna2[1] + (repeat * distance[1])
    )

    upper_in_range = (upper_boundaries[0] >= 0 and upper_boundaries[0] < HEIGHT) and (
        upper_boundaries[1] >= 0 and upper_boundaries[1] < WIDTH
    )

    lower_in_range = (lower_boundaries[0] >= 0 and lower_boundaries[0] < HEIGHT) and (
        lower_boundaries[1] >= 0 and lower_boundaries[1] < WIDTH
    )

    if upper_in_range or lower_in_range:
        if upper_in_range and not lower_in_range:
            update_map(upper_boundaries)
            return {"status": True, "antinodes": [upper_boundaries]}
        elif not upper_in_range and lower_in_range:
            update_map(lower_boundaries)
            return {"status": True, "antinodes": [lower_boundaries]}
        elif upper_in_range and lower_in_range:
            update_map(upper_boundaries)
            update_map(lower_boundaries)
            return {"status": True, "antinodes": [upper_boundaries, lower_boundaries]}
    else:
        return {"status": False, "antinodes": []}


total = set()

for freq, antenna_list in antennas.items():
    if len(antenna_list) < 2:
        continue

    for antenna1, antenna2 in itertools.combinations(antenna_list, r=2):
        total.add(tuple(antenna1))
        total.add(tuple(antenna2))

        distance = distance_between_antennas(antenna1, antenna2)

        repeat = 1

        while True:
            inrange = in_range([antenna1, antenna2], distance, repeat)
            if not inrange["status"]:
                break
            for point in inrange["antinodes"]:
                total.add(point)
            
            repeat += 1


        # y_distance = antenna2[0] - antenna1[0]
        # x_distance = antenna2[1] - antenna1[1]

        # lower_antinode = (antenna2[0] + (y_distance)), (antenna2[1] + (x_distance))
        # upper_antinode = (antenna1[0] - (y_distance)), (antenna1[1] - (x_distance))

        # upper_antinode_in_range = (
        #     upper_antinode[0] >= 0 and upper_antinode[0] < height
        # ) and (upper_antinode[1] >= 0 and upper_antinode[1] < width)

        # lower_antinode_in_range = (
        #     lower_antinode[0] >= 0 and lower_antinode[0] < height
        # ) and (lower_antinode[1] >= 0 and lower_antinode[1] < width)

        # while upper_antinode_in_range or lower_antinode_in_range:

        # if upper_antinode[0] >= 0 and upper_antinode[0] < height:
        #     if upper_antinode[1] >= 0 and upper_antinode[1] < width:
        #         text = result_antinodes[upper_antinode[0]]
        #         result_antinodes[upper_antinode[0]] = (
        #             text[: upper_antinode[1]] + "#" + text[upper_antinode[1] + 1 :]
        #         )
        #         total.add(upper_antinode)
        # if lower_antinode[0] >= 0 and lower_antinode[0] < height:
        #     if lower_antinode[1] >= 0 and lower_antinode[1] < width:
        #         text = result_antinodes[lower_antinode[0]]
        #         result_antinodes[lower_antinode[0]] = (
        #             text[: lower_antinode[1]] + "#" + text[lower_antinode[1] + 1 :]
        #         )
        #         total.add(lower_antinode)

pprint.pprint(result_antinodes)
print(len(total))
