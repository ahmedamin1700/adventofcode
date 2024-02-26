COLORS_MAP = {
    "red": 12,
    "green": 13,
    "blue": 14
}

filename = "input.txt"

file = open(filename, "r")
lines = file.readlines()


def generate_games(data):
    gs = []

    for line in data:
        data = line.split(":")[1].strip()

        game = [
            [
                [
                    entry.strip() for entry in trial.strip().split(" ")
                ] for trial in row.strip().split(",")
            ] for row in data.split(";")
        ]
        gs.append(game)
    return gs


def count_valid_ids(plays):
    count = 0

    for i, game in enumerate(plays):
        win = True
        for trial in game:
            for entry in trial:
                if COLORS_MAP[entry[1]] < int(entry[0]):
                    win = False
                    break

            if not win:
                break
        if win:
            count += i + 1
    return count

def power_of_cubes(plays):
    result = 0

    for i, game in enumerate(plays):
        colors = {
            "red": 1,
            "green": 1,
            "blue": 1
        }
        total = 1

        for trial in game:
            for entry in trial:
                if colors[entry[1]] < int(entry[0]):
                    colors[entry[1]] = int(entry[0])
        
        for value in colors.values():
            total *= value
        
        result += total

    return result


games = generate_games(lines)
result = count_valid_ids(games)
powerofcubes = power_of_cubes(games)