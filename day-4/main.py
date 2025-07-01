# --- Day 4: Ceres Search ---
class Ceres:

    def __init__(self, file_path):
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        self.grid = lines
        self.count = 0

    def count_horizontally(self) -> None:

        for line in self.grid:
            self.count += line.count("XMAS")

            self.count += line.count("SAMX")

    def count_vertically(self) -> None:

        # count from up to down
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):

                if x + 3 < len(self.grid):
                    word = (
                        self.grid[x][y]
                        + self.grid[x + 1][y]
                        + self.grid[x + 2][y]
                        + self.grid[x + 3][y]
                    )
                    if word == "XMAS" or word == "SAMX":
                        self.count += 1

    def count_diagonally(self) -> None:

        # count from top to bottom
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):

                # moving right down
                if x + 3 <= len(self.grid) - 1 and y + 3 <= len(self.grid[x]) - 1:
                    word = (
                        self.grid[x][y]
                        + self.grid[x + 1][y + 1]
                        + self.grid[x + 2][y + 2]
                        + self.grid[x + 3][y + 3]
                    )
                    if word == "XMAS":
                        self.count += 1

                # moving right up
                if x - 3 >= 0 and y + 3 <= len(self.grid[x]) - 1:
                    word = (
                        self.grid[x][y]
                        + self.grid[x - 1][y + 1]
                        + self.grid[x - 2][y + 2]
                        + self.grid[x - 3][y + 3]
                    )
                    if word == "XMAS":
                        self.count += 1

                # moving left down
                if x + 3 <= len(self.grid) - 1 and y - 3 >= 0:
                    word = (
                        self.grid[x][y]
                        + self.grid[x + 1][y - 1]
                        + self.grid[x + 2][y - 2]
                        + self.grid[x + 3][y - 3]
                    )
                    if word == "XMAS":
                        self.count += 1

                # moving left up
                if x - 3 >= 0 and y - 3 >= 0:
                    word = (
                        self.grid[x][y]
                        + self.grid[x - 1][y - 1]
                        + self.grid[x - 2][y - 2]
                        + self.grid[x - 3][y - 3]
                    )
                    if word == "XMAS":
                        self.count += 1

    def count_xmas(self) -> int:
        total = 0
        diagonals = ["S", "M"]

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "A":
                    if (
                        row - 1 >= 0
                        and col - 1 >= 0
                        and row + 1 < len(self.grid)
                        and col + 1 < len(self.grid[row])
                    ):
                        upper_left = self.grid[row - 1][col - 1]
                        lower_right = self.grid[row + 1][col + 1]
                        lower_left = self.grid[row + 1][col - 1]
                        upper_right = self.grid[row - 1][col + 1]

                        if (
                            upper_left in diagonals
                            and lower_right in diagonals
                            and upper_left != lower_right
                            and lower_left in diagonals
                            and upper_right in diagonals
                            and lower_left != upper_right
                        ):
                            total += 1
        return total


ceres = Ceres("day-4/input.txt")
# ceres.count_horizontally()
# ceres.count_vertically()
# ceres.count_diagonally()
total = ceres.count_xmas()

print(total)
