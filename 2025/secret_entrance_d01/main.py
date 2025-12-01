from typing import Tuple, List, Dict
import os

# from 0 to 99  total is 100.
N = 100
STARTING_POINT = 50


def process_move(point: int, direction: str, times: int) -> Tuple[int, int]:
    """
    Simulates every single click and counts how many times the dial lands exactly on 0.

    Args:
        point (int): current or starting point to process moving from.
        direction (str): which direction to move to "L" or "R".
        times (int): how many times to process moving to that direction.

    Returns:
        Tuple[int, int]: end point after process moving and count of how many times crossed or reached 0.
    """
    count_of_zero_hit = 0
    current_point = point

    for _ in range(times):
        if direction == "L":
            current_point = (current_point - 1 + N) % N
        elif direction == "R":
            current_point = (current_point + 1) % N

        # This check happens AFTER every single click of the dial.
        if current_point == 0:
            count_of_zero_hit += 1

    return current_point, count_of_zero_hit


def analyze(filename: str) -> int:
    """
    Reads moves from a file and counts cumulative zero crossings for Part Two.

    Args:
        filename (str): filename path of the input for directions and move times.

    Returns:
        int: how many times crossed or reached 0 after all rotations.
    """
    rotations_data: List[Dict] = []

    try:
        script_dir = os.path.dirname(__file__)
        full_path = os.path.join(script_dir, filename)

        with open(full_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                direction = line[0]
                times = int(line[1:])
                rotations_data.append({"direction": direction, "times": times})

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found at location: {full_path}")
        return 0
    except (ValueError, IndexError) as e:
        print(f"Error processing line ({line if 'line' in locals() else 'N/A'}): {e}")
        return 0

    count = 0
    current_point = STARTING_POINT

    for rotation in rotations_data:
        point, c = process_move(current_point, rotation["direction"], rotation["times"])
        current_point = point
        count += c

    return count


def main():
    filename = "input/input.txt"
    count = analyze(filename)
    print(f"Total boundary crossings (Part Two): {count}")


if __name__ == "__main__":
    main()
