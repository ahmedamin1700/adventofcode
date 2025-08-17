# --- Day 9: Disk Fragmenter --- Part 1

from typing import List

# Define a constant for the input file path for easier management.
INPUT_FILE = "day-9/input.txt"
DEFAULT_INPUT = "2333133121414131402"

# Use a constant to represent free space ("dots") for better readability.
FREE_SPACE_MARKER = -1


def get_data(filepath: str) -> List[int]:
    """
    Reads a single line of digits from the input file and converts it to a list of integers.

    Args:
        filepath (str): The path to the input file.

    Returns:
        List[int]: A list of integers from the file.
                   Returns a default list if the file is not found or is empty.
    """
    try:
        with open(filepath, "r") as file:
            content = file.read().strip()
            if not content:
                # Handle the case where the file is empty.
                print(f"Warning: '{filepath}' is empty. Using default data.")
                return [int(digit) for digit in DEFAULT_INPUT]
            return [int(digit) for digit in content]
    except FileNotFoundError:
        print(f"Warning: '{filepath}' not found. Using default data.")
        return [int(digit) for digit in DEFAULT_INPUT]
    except ValueError:
        # Handle cases where the file contains non-digit characters.
        print(f"Error: '{filepath}' contains non-digit characters. Exiting.")
        exit(1)  # Exit the script as the input is invalid.


def build_disk_map(raw_data: List[int]) -> List[int]:
    """
    Converts the raw data list into a disk map representation.

    File blocks are represented by their zero-based ID, and free space
    is represented by the FREE_SPACE_MARKER (-1).

    Args:
        raw_data (List[int]): The list of integers representing file and space lengths.

    Returns:
        List[int]: The fully constructed disk map.
    """
    disk_map = []
    file_id_counter = 0

    for i, length in enumerate(raw_data):
        is_file_block = i % 2 == 0

        if is_file_block:
            # Append the file block with its corresponding ID.
            disk_map.extend([file_id_counter] * length)
            file_id_counter += 1
        else:
            # Append the free space blocks.
            disk_map.extend([FREE_SPACE_MARKER] * length)

    return disk_map


def compact_disk(disk_map: List[int]) -> List[int]:
    """
    Compacts the disk by moving file blocks from the end to the first available free space.
    This function modifies the list in-place for efficiency but also returns it.

    Args:
        disk_map (List[int]): The disk map to be compacted.

    Returns:
        List[int]: The compacted disk map.
    """
    # Pointer to find the leftmost free space.
    left_pointer = 0
    # Pointer to find the rightmost file block.
    right_pointer = len(disk_map) - 1

    while left_pointer < right_pointer:
        # Find the next free space from the left.
        if disk_map[left_pointer] != FREE_SPACE_MARKER:
            left_pointer += 1
            continue

        # Find the next file block from the right.
        # This also correctly handles trimming trailing free space.
        if disk_map[right_pointer] == FREE_SPACE_MARKER:
            right_pointer -= 1
            continue

        # Move the rightmost file block to the leftmost free space.
        disk_map[left_pointer] = disk_map[right_pointer]

        # The original position of the rightmost block is now considered free.
        # This simplifies logic, as we only need to "move" and not "swap".
        # The right pointer will naturally move past this spot in the next iteration.
        right_pointer -= 1
        left_pointer += 1

    # After the loop, trim any remaining trailing free space markers.
    final_length = right_pointer + 1
    return disk_map[:final_length]


def calculate_checksum(disk_map: List[int]) -> int:
    """
    Calculates the filesystem checksum.

    The checksum is the sum of (block_position * file_id) for all file blocks.

    Args:
        disk_map (List[int]): The final, compacted disk map.

    Returns:
        int: The calculated checksum.
    """
    return sum(i * val for i, val in enumerate(disk_map) if val != FREE_SPACE_MARKER)


def main():
    """Main function to run the disk fragmentation and checksum process."""
    # 1. Get and parse the input data.
    raw_data = get_data(INPUT_FILE)

    # 2. Build the initial disk map from the raw data.
    initial_disk = build_disk_map(raw_data)

    # 3. Compact the disk according to the specified process.
    compacted_disk = compact_disk(initial_disk)

    # 4. Calculate the final checksum from the compacted disk.
    checksum = calculate_checksum(compacted_disk)

    print(f"The resulting filesystem checksum is: {checksum}")


if __name__ == "__main__":
    main()
