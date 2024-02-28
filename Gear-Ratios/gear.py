"""
Advent the code.
Gear Ratios v1.
"""
from collections import defaultdict
from typing import List, Tuple

from helpers import get_adjacent_positions

file = open('input.txt', 'r')
lines = file.readlines()

# convert input to grid of chars.
GRID = [list(line.strip()) for line in lines]
HEIGHT = len(GRID)
WIDTH = len(GRID[0])
# create grid of True or False 'part number'.
IS_PART_NUMBER = [[False for _ in range(WIDTH)] for __ in range(HEIGHT)]

GEAR_IDS = [[0 for _ in range(WIDTH)] for __ in range(HEIGHT)]
ID = 1


def mark_part_numbers(row: int, column: int) -> None:
    """
    mark all adjacent chars to a symbol to be a part numbers.
    :param row: row index of char.
    :param column: column index of char.
    :return: None
    """
    global GRID, GEAR_IDS, ID

    queue = [(row, column)]
    i = 0

    while i < len(queue):
        x, y = queue[i]
        if GRID[x][y].isdigit():
            GEAR_IDS[x][y] = ID

        for adj_r, adj_c in get_adjacent_positions(x, y, WIDTH, HEIGHT):
            if GRID[adj_r][adj_c].isdigit() and not GEAR_IDS[adj_r][adj_c]:
                queue.append((adj_r, adj_c))

        i += 1


def extract_part_numbers() -> list[int]:
    """
    extract all part numbers which is marked True in IS_PART_NUMBER grid.
    :return: list of integers.
    """
    global GRID, IS_PART_NUMBER, HEIGHT, WIDTH

    numbers = []
    current_number = ''

    for row in range(HEIGHT):
        for column in range(WIDTH):
            if IS_PART_NUMBER[row][column]:
                current_number += GRID[row][column]
            elif current_number:
                numbers.append(int(current_number))
                current_number = ''

        if current_number:
            numbers.append(int(current_number))
            current_number = ''
    return numbers


def extract_possible_gears() -> dict[int, list[int]]:
    global GRID, GEAR_IDS, HEIGHT, WIDTH

    possible_gears = defaultdict(list)
    current_number = ''
    id = -1

    for r in range(HEIGHT):
        for c in range(WIDTH):
            if GEAR_IDS[r][c]:
                id = GEAR_IDS[r][c]
                current_number += GRID[r][c]
            elif current_number:
                possible_gears[id].append(int(current_number))
                id = -1
                current_number = ''
        if current_number:
            possible_gears[id].append(int(current_number))
            id = -1
            current_number = ''
    return possible_gears


def extract_real_gears(possible_gears: dict[int, list[int]]) -> list[tuple[int, int]]:
    gears = []

    for part_numbers in possible_gears.values():
        if len(part_numbers) == 2:
            gears.append(tuple(part_numbers))
    return gears


def main():
    global ID
    for r in range(HEIGHT):
        for c in range(WIDTH):
            char = GRID[r][c]

            # check if the char is a '*' symbol.
            if char == '*':
                mark_part_numbers(r, c)
                ID += 1

    possible_gears = extract_possible_gears()
    gears = extract_real_gears(possible_gears)

    gears_ratios = [gear[0] * gear[1] for gear in gears]
    print(sum(gears_ratios))


if __name__ == '__main__':
    main()
