def blink(line: list[int], times: int) -> int:
    current_state = line
    print("Initial arrangement:")
    print_line(current_state)
    for t in range(times):
        blinked = []
        for num in current_state:
            if num == 0:
                blinked.append(1)
            elif len(str(num)) % 2 == 0:
                num_str = str(num)
                length = len(num_str)
                half = length / 2

                blinked.append(int(num_str[: int(half)]))
                blinked.append(int(num_str[int(half) :]))
            else:
                blinked.append(num * 2024)
        current_state = blinked
        print(f"After {t + 1} blink{'s' if t + 1 > 1 else ''}:")
        print_line(current_state)
    return len(current_state)


def print_line(line: list[int]):
    for num in line:
        print(num, " ", end="")
    print()


def main():
    filename = "day-11/test.txt"
    with open(filename, "r") as file:
        line = [int(num) for num in file.readlines()[0].strip().split(" ")]

    stones_num = blink(line, 25)
    print(f"\nafter 25 blinks found {stones_num} stones.")


if __name__ == "__main__":
    main()
