import os
import time

class Guard:
    DIRECTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    DELTAS = {'UP': (-1, 0), 'RIGHT': (0, 1), 'DOWN': (1, 0), 'LEFT': (0, -1)}
    START_CHARS = {'^': 'UP', '>': 'RIGHT', 'v': 'DOWN', '<': 'LEFT'}

    def __init__(self, file_path):
        with open(file_path) as file:
            # Read the initial state of the grid
            initial_grid = [list(line.strip()) for line in file]

        self.height = len(initial_grid)
        self.width = len(initial_grid[0])
        
        self.start_row, self.start_col, self.start_direction = self._find_start_state(initial_grid)
        
        self.original_grid = [row[:] for row in initial_grid]

        self.grid = [row[:] for row in initial_grid]
        if self.start_row is not None:
            self.grid[self.start_row][self.start_col] = '.'

    def _find_start_state(self, grid_to_search):
        # This method now takes a grid as an argument to be more flexible
        for r, row_data in enumerate(grid_to_search):
            for c, char in enumerate(row_data):
                if char in self.START_CHARS:
                    return r, c, self.START_CHARS[char]
        return None, None, None

    def _is_on_map(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def _print_debug_frame(self, grid_to_print, r, c, direction, step_count):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Step: {step_count} | Position: ({r}, {c}) | Direction: {direction}")
        print("-" * self.width)
        display_grid = [row[:] for row in grid_to_print]
        guard_symbol = [k for k, v in self.START_CHARS.items() if v == direction][0]
        if self._is_on_map(r, c):
            display_grid[r][c] = guard_symbol
        for row in display_grid:
            print("".join(row))
        print("-" * self.width)

    def run_simulation(self):
        r, c, direction = self.start_row, self.start_col, self.start_direction
        visited_positions = set()
        
        while self._is_on_map(r, c):
            visited_positions.add((r, c))
            
            dr, dc = self.DELTAS[direction]
            next_r, next_c = r + dr, c + dc
            
            is_out_range = not self._is_on_map(next_r, next_c)
            if is_out_range:
                break
            
            is_obstructed = self.grid[next_r][next_c] == '#'
            if is_obstructed:
                current_dir_index = self.DIRECTIONS.index(direction)
                direction = self.DIRECTIONS[(current_dir_index + 1) % 4]
            else:
                r, c = next_r, next_c
                
        return visited_positions
    
    def _does_it_loop(self, grid_to_test):
        """Runs a simulation and returns True if a loop is detected."""
        # FIX: Reset direction to the *start* direction, not the last known direction.
        r, c, direction = self.start_row, self.start_col, self.start_direction
        history = set()

        # A safety limit to prevent accidental true infinite loops in our code.
        for _ in range(self.height * self.width * 4 + 1):
            if not self._is_on_map(r, c):
                return False # Guard walked off the map.

            current_state = (r, c, direction)
            if current_state in history:
                return True # Loop detected!
            history.add(current_state)

            dr, dc = self.DELTAS[direction]
            next_r, next_c = r + dr, c + dc
            
            is_out_range = not self._is_on_map(next_r, next_c)
            if is_out_range:
                break
            
            is_obstructed = grid_to_test[next_r][next_c] == '#'
            
            if is_obstructed:
                current_dir_index = self.DIRECTIONS.index(direction)
                direction = self.DIRECTIONS[(current_dir_index + 1) % 4]
            else:
                r, c = next_r, next_c
    
        return False # Exceeded max steps, no loop found.
    
    def count_looping_placements(self):
        """Tests all valid empty spots to see if placing an obstacle creates a loop."""
        candidate_placements = self.run_simulation()
        candidate_placements.remove((self.start_row, self.start_col))

        loop_count = 0
        total_candidates = len(candidate_placements)
        print(f"Found {total_candidates} candidate locations to test.")

        for i, (r, c) in enumerate(candidate_placements):
            # A simple progress indicator is very helpful for long runs.
            print(f"Testing candidate {i+1}/{total_candidates} at ({r}, {c})...", end='\r')
        
            temp_grid = [row[:] for row in self.original_grid]
            temp_grid[r][c] = '#'

            if self._does_it_loop(temp_grid):
                loop_count += 1
            
        print("\nTesting complete.                ") 
        return loop_count

print("--- Solving Part One ---")
guard_p1 = Guard("day-6/input.txt")
locations_visited = guard_p1.run_simulation()
print(f"Answer for Part One: {len(locations_visited)}")

print("\n" + "="*25 + "\n")

print("--- Solving Part Two ---")
guard_p2 = Guard("day-6/input.txt")
total_looping_placements = guard_p2.count_looping_placements()
print(f"Answer for Part Two: {total_looping_placements}")