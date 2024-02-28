"""
Advent the code.
Gear Ratios v1.
"""

from helpers import get_adjacent_positions

file = open('input.txt', 'r')
lines = file.readlines()

# convert input to grid of chars.
GRID = [list(line.strip()) for line in lines]
HEIGHT = len(GRID)
WIDTH = len(GRID[0])
# create grid of True or False 'part number'.
IS_PART_NUMBER = [[False for _ in range(WIDTH)] for __ in range(HEIGHT)]


def mark_part_numbers(row: int, column: int) -> None:
    """
    mark all adjacent chars to a symbol to be a part numbers.
    :param row: row index of char.
    :param column: column index of char.
    :return: None
    """
    global GRID, IS_PART_NUMBER

    queue = [(row, column)]
    i = 0

    while i < len(queue):
        x, y = queue[i]
        if GRID[x][y].isdigit():
            IS_PART_NUMBER[x][y] = True

        for adj_r, adj_c in get_adjacent_positions(x, y, WIDTH, HEIGHT):
            if GRID[adj_r][adj_c].isdigit() and not IS_PART_NUMBER[adj_r][adj_c]:
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

def main():
    for r in range(HEIGHT):
        for c in range(WIDTH):
            char = GRID[r][c]

            # check if the char is a symbol.
            if char != '.' and not char.isdigit():
                mark_part_numbers(r, c)

    part_numbers = extract_part_numbers()
    print(sum(part_numbers))

if __name__ == '__main__':
    main()
