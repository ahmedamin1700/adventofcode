import itertools

with open("day-7/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    lines = [line.split(":") for line in lines]

equations = []

for line in lines:
    data = {
        "total": int(line[0]),
        "numbers": list(map(int, line[1].strip().split(" "))),
        "status": False
    }
    equations.append(data)

# print(equations)

def evaluate_left_to_right(numbers: list[int], ops: tuple[str]) -> int:
    total = numbers[0]

    for i in range(len(ops)):
        operator = ops[i]
        next_number = numbers[i + 1]

        if operator == "+":
            total += next_number
        elif operator == "*":
            total *= next_number
        elif operator == "||":
            total = int(str(total) + str(next_number))
    
    return total


def calculate_all_operations(total: int, numbers: list[int]) -> bool:
    operations = ["+", "*", "||"]
    operations_numbers = len(numbers) - 1

    operator_combinations = itertools.product(operations, repeat=operations_numbers)

    for ops in operator_combinations:
        result = evaluate_left_to_right(numbers, ops)

        if total == result:
            return True
    
    return False



# loop through each equation
for equation in equations:
    result = calculate_all_operations(equation["total"], equation["numbers"])
    equation["status"] = result

total = sum([equation["total"] for equation in equations if equation["status"] == True])
# apply each
print(total)