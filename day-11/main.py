from functools import cache


@cache
def count(stone: int, times: int):
    if times == 0:
        return 1
    elif stone == 0:
        return count(1, times - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[: length // 2]), times - 1) + count(
            int(string[length // 2 :]), times - 1
        )
    return count(stone * 2024, times - 1)


def blink(stones: list[int], times: int) -> int:
    return sum(count(stone, times) for stone in stones)


def main():
    filename = "day-11/test.txt"
    try:
        with open(filename, "r") as file:
            line_str = file.read().strip().replace("\n", " ").split()
            line = [int(num) for num in line_str if num]

        stones_num = blink(line, 75)
        print(f"\nafter final blinks found {stones_num} stones.")
    except FileNotFoundError:
        print(f"Error: the file name {filename} not found.")
    except MemoryError:
        print("Memory error: The list became too large for your system RAM.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
