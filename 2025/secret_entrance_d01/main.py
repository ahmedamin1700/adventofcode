ROTATIONS = []
starting_point = 50


def analyze(filename: str) -> int:
    try:
        with open(filename, "r") as file:
            rotations_str = [line.strip() for line in file.readlines()]
            for rotation in rotations_str:
                direction = rotation[0]
                times = int(rotation[1:])
                ROTATIONS.append({"direction": direction, "times": times})
    except FileNotFoundError:
        print(f"Error: file {filename} not found")

    count = 0
    current_point = starting_point

    for rotation in ROTATIONS:
        point = 0
        if current_point == 0:
            count += 1
        if rotation["direction"] == "L":
            point = current_point - rotation["times"]
        if rotation["direction"] == "R":
            point = current_point + rotation["times"]

        current_point = point % 100

    return count


def main():
    filename = "input/input.txt"
    count = analyze(filename)
    print(count)


if __name__ == "__main__":
    main()
