from typing import List, Tuple
import numpy as np


class Map:
    def __init__(self, filename: str) -> None:
        self.map = []
        self.trialheads = []
        self.filename = filename
        self.read_map()
        self.find_trialheads()

    def read_map(self) -> None:
        try:
            with open(self.filename, "r") as file:
                self.map = np.array(
                    [[int(item) for item in row.strip()] for row in file.readlines()]
                )
        except FileNotFoundError as e:
            print(f"{e}")

    def find_trialheads(self, item: int = 0) -> None:
        """Finds all trailheads in the map at instance initialization

        Args:
            item (int, optional): first point height. Defaults to 0.
        """
        indices = np.where(self.map == item)
        self.trialheads = [(int(row), int(col)) for row, col in list(zip(*indices))]

    def find_valid_hiking_neighbors(
        self, point: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """Returns a list of valid neighboring coordinates (row, col) as ints,
        handling boundaries automatically and check exactly the "+1" rule.

        Args:
            point (Tuple[int, int]): point where to look for neighbors.

        Returns:
            List[Tuple[int, int]]: list of all valid neighbors.
        """
        row, col = point
        current_height = self.map[row][col]

        potential_moves = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        valid_neighbors = []

        map_height = len(self.map)
        map_width = len(self.map[0])

        for r, c in potential_moves:
            if 0 <= r < map_height and 0 <= c < map_width:
                if self.map[r][c] == current_height + 1:
                    valid_neighbors.append((r, c))

        return valid_neighbors

    def calculate_trailhead_score(self, start_coords: Tuple[int, int]) -> int:
        """Move through each path from the start_coords.

        Args:
            start_coords (Tuple[int, int]):

        Returns:
            int: how many 9s found from this start_coords.
        """
        queue = []
        visited_coords = set()
        reached_nines = set()

        queue.append(start_coords)
        visited_coords.add(start_coords)

        while len(queue) != 0:
            current_coords = queue.pop()

            valid_neighbors = self.find_valid_hiking_neighbors(current_coords)

            for neighbor in valid_neighbors:
                if neighbor not in visited_coords:
                    neighbor_height = self.map[neighbor[0]][neighbor[1]]

                    if neighbor_height == 9:
                        reached_nines.add(neighbor)
                        continue
                    visited_coords.add(neighbor)
                    queue.append(neighbor)

        return len(reached_nines)


def main():
    map = Map("day-10/test.txt")

    total = 0

    for trial in map.trialheads:
        score = map.calculate_trailhead_score(trial)
        total += score

    print(total)


if __name__ == "__main__":
    main()
