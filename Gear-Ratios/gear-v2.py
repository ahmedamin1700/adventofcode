"""
Advent the code.
Gear Ratios v2.
"""

from helpers import get_adjacent_positions

FILE = 'input.txt'


file = open(FILE, 'r')
lines = file.readlines()

GRID = [list(line.strip()) for line in lines]
HEIGHT = len(lines)
WIDTH = len(lines[0].strip())


def number_from_digits(d: list[str]):
    return int(''.join(d))


part_number_sum = 0

for row in range(HEIGHT):
    digits = []
    adjacent = False

    for column in range(WIDTH):
        char = lines[row][column]

        # check if the char is digit.
        if char.isdigit():
            digits.append(char)

            # continue if we already know that the number adjacent to a symbol.
            if adjacent:
                continue

            # check for a symbol in all possible adjacent directions.
            for adj_r, adj_c in get_adjacent_positions(row, column, WIDTH, HEIGHT):
                char = GRID[adj_r][adj_c]
                # find a symbol which is not '.' and not digit.
                if not adjacent and char != '.' and not char.isdigit():
                    adjacent = True
                    break

        else:
            if adjacent:
                part_number_sum += number_from_digits(digits)
            digits = []
            adjacent = False
    # cases where part number in the end of the line.
    if adjacent:
        part_number_sum += number_from_digits(digits)

print(part_number_sum)
