def generate_invalid_ids(max_number: int):
    """
    Generates a set of all possible invalid IDs up to a given maximum number.
    An invalid ID is a sequence of digits repeated at least twice.
    """
    generated_ids = set()

    # Determine the longest possible base sequence we need to check.
    max_base_length = len(str(max_number)) // 2

    for base_length in range(1, max_base_length + 1):
        # Also, handle the single-digit case explicitly for clarity.
        if base_length == 1:
            start_num = 1
        else:
            start_num = 10 ** (base_length - 1)

        end_num = (10**base_length) - 1

        for base_num in range(start_num, end_num + 1):
            base_num_str = str(base_num)

            # Start by repeating the base sequence twice.
            current_repeated_str = 2 * base_num_str

            while True:
                generated_num = int(current_repeated_str)

                # If the generated number exceeds our limit, we can stop for this base.
                if generated_num > max_number:
                    break

                generated_ids.add(generated_num)

                # Add another repetition for the next loop iteration.
                current_repeated_str += base_num_str

    return generated_ids


def analyze(filename: str):
    """
    Parses ranges from a file, finds all invalid IDs within those ranges,
    and returns their sum.
    """
    ranges = []
    try:
        with open(filename, "r") as file:
            line = file.read().strip()  # Use read() and strip() for cleaner parsing
            string_ranges = line.split(",")
            for r_str in string_ranges:
                if "-" in r_str:
                    start_str, end_str = r_str.split("-")
                    start_num = int(start_str)
                    end_num = int(end_str)
                    ranges.append((start_num, end_num))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0  # Return 0 or raise an exception on error

    # Find the absolute maximum ID from all ranges.
    max_id = 0
    for start_val, end_val in ranges:
        if end_val > max_id:
            max_id = end_val

    # Generate all possible invalid IDs up to that maximum.
    all_possible_invalids = generate_invalid_ids(max_id)

    # Use a set for the final IDs to ensure uniqueness, just in case.
    final_invalid_ids = set()

    # Check which generated IDs fall into any of our ranges.
    for invalid_id in all_possible_invalids:
        for start_range, end_range in ranges:
            if start_range <= invalid_id <= end_range:
                final_invalid_ids.add(invalid_id)
                # Once found in a range, no need to check other ranges.
                break

    return sum(final_invalid_ids)


def main():
    filename = "input/input.txt"
    total = analyze(filename)
    print(f"The sum of all invalid IDs is: {total}")


if __name__ == "__main__":
    main()
