def analyze(filename: str):
    ids = []
    invalid_ids = []

    try:
        with open(filename, "r") as file:
            line = file.readlines()[0]

            ids = line.split(",")

            # print(ids)
    except FileNotFoundError:
        print(f"File {filename} not found.")

    for id in ids:
        start = id.split("-")[0]
        end = id.split("-")[1]

        for i in range(int(start), int(end) + 1):
            length = len(str(i))
            if length % 2 == 0:
                i_str = str(i)
                if i_str[: length // 2] == i_str[length // 2 :]:
                    invalid_ids.append(i)

    print(sum(invalid_ids))


def main():
    filename = "input/input.txt"
    analyze(filename)


if __name__ == "__main__":
    main()
