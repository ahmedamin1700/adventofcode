# --- Day 1: Historian Hysteria ---

file_path = 'day-1/input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

sides = [side.split('   ') for side in [line.strip() for line in lines]]

left = sorted([int(side[0]) for side in sides])
right = sorted([int(side[1]) for side in sides])

total_distance = sum(abs(l - r) for l, r in zip(left, right))

print(total_distance)

similarity_score = sum(l * right.count(l) for l in left)

print(similarity_score)