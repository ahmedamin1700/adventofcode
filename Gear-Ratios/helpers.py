from itertools import product


def is_in_bound(row: int, column: int, w: int, h: int) -> bool:
    """
    :param row: row index for the char.
    :param column: column index of the char.
    :param w: the total width of the grid.
    :param h: the total height of the grid.
    :return: if char is in the boundary or not.
    """
    return (0 <= row < h) and (0 <= column < w)


def get_adjacent_positions(row: int, column: int, w: int, h: int) -> list[tuple[int, int]]:
    """
    :param row: row index for the char.
    :param column: column index of the char.
    :param w: the total width of the grid.
    :param h: the total height of the grid.
    :return: list of tuples for all adjacent chars positions.
    """
    offset = [1, 0, -1]
    adjacent_positions = []

    for row_offset, col_offset in product(offset, offset):
        if row_offset or col_offset:
            adj_row = row + row_offset
            adj_col = column + col_offset

            if is_in_bound(adj_row, adj_col, w, h):
                adjacent_positions.append((adj_row, adj_col))
    return adjacent_positions
