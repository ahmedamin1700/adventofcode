from typing import Tuple, List, Dict, Set


class GardenAnalyzer:
    """
    Analyzes a garden represented by a grid of characters, calculating the area and
    perimeter for each contiguous plot of the same type.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initializes the GardenAnalyzer by reading the garden map from a file.

        Args:
            file_path: The path to the file containing the garden map.
        """
        self.file_path = file_path
        self.plot_map: List[List[str]] = []  # Stores the grid of plot types
        self.plot_details: List[Dict] = []  # Stores the calculated details for each plot

        try:
            with open(self.file_path, "r") as file:
                # Read the file and create a 2D list of characters
                self.plot_map = [
                    [char for char in line.strip()] for line in file.readlines()
                ]
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            # Re-raise for the caller to handle if necessary
            raise
        except Exception as e:
            # Catch other potential file reading errors
            raise e

        # Determine the dimensions of the garden map
        self.height = len(self.plot_map)
        # Assumes at least one row exists
        self.width = len(self.plot_map[0])

    def _get_plot_neighbors_and_fence_length(
        self, location: Tuple[int, int]
    ) -> Tuple[int, List[Tuple[int, int]]]:
        """
        Calculates the number of fence segments needed for a specific plot location
        and identifies neighboring locations within the same plot.

        A fence segment is added if a neighbor is a different plot type or is outside
        the garden boundaries.

        Args:
            location: The (row, column) coordinates of the current location.

        Returns:
            A tuple containing:
            - The number of valid fence segments for this location.
            - A list of coordinates for adjacent locations of the same plot type.
        """
        row, col = location
        current_plot_type = self.plot_map[row][col]

        # Define potential surrounding locations (up, down, left, right)
        surrounding_locations = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        fence_segment_count = 0
        same_type_neighbors: List[Tuple[int, int]] = []

        for r, c in surrounding_locations:
            # Check if the neighbor is within the garden boundaries
            if 0 <= r < self.height and 0 <= c < self.width:
                # If the neighbor is a different type, a fence segment is needed
                if self.plot_map[r][c] != current_plot_type:
                    fence_segment_count += 1
                # If the neighbor is the same type, add to the neighbor list for expansion
                else:
                    same_type_neighbors.append((r, c))
            else:
                # If the neighbor is outside boundaries, a fence segment is needed
                fence_segment_count += 1

        return fence_segment_count, same_type_neighbors

    def analyze_plots(self) -> None:
        """
        Identifies all distinct plots in the garden and calculates their total area
        and perimeter using a Breadth-First Search (BFS) approach.

        The results are stored in the `self.plot_details` list.
        """
        # A set to keep track of locations that have already been processed to
        # avoid redundant work and infinite loops.
        visited_locations: Set[Tuple[int, int]] = set()

        for row in range(self.height):
            for col in range(self.width):
                current_location = (row, col)

                # Only start processing if this location hasn't been visited yet
                if current_location not in visited_locations:
                    current_plot_area = 0
                    current_plot_perimeter = 0
                    # A queue (implemented as a set for quick lookup and removal)
                    # for managing locations within the current plot to visit.
                    queue: Set[Tuple[int, int]] = {current_location}

                    # Process all locations in the current contiguous plot
                    while queue:
                        # Pop an arbitrary location from the set (mimics queue/stack behavior)
                        loc = queue.pop()

                        # If already visited in this or a previous run, skip it
                        if loc in visited_locations:
                            continue

                        # Mark the location as visited
                        visited_locations.add(loc)
                        current_plot_area += 1

                        # Get fence count and same-type neighbors for this location
                        count, neighbors = self._get_plot_neighbors_and_fence_length(loc)
                        current_plot_perimeter += count

                        # Add unvisited neighbors to the queue for processing
                        for neighbor_loc in neighbors:
                            if neighbor_loc not in visited_locations:
                                queue.add(neighbor_loc)

                    # Store the details of the complete plot once the queue is empty
                    self.plot_details.append(
                        {
                            "plot_type": self.plot_map[row][col],
                            "area": current_plot_area,
                            "perimeter": current_plot_perimeter,
                        }
                    )

    def calculate_total_price(self) -> int:
        """
        Calculating the total price by multiplying that region's (plot) area by its perimeter.

        Returns:
            int: total price of all plots fences.
        """
        return sum([plot["area"] * plot["perimeter"] for plot in self.plot_details])

def main():
    # Example usage
    filename = "day-12/input.txt"
    try:
        # Create an instance of the analyzer
        garden_analyzer = GardenAnalyzer(filename)
        # Run the analysis
        garden_analyzer.analyze_plots()
        # Print the results
        print(f"The total price of fencing all regions on the map: ", garden_analyzer.calculate_total_price())
    except FileNotFoundError:
        print(f"Analysis aborted due to missing file: {filename}")
    except Exception as e:
        print(f"An unexpected error occurred during garden analysis: {e}")


if __name__ == "__main__":
    main()
