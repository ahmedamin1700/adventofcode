# --- Day 2: Red-Nosed Reports ---

file_path = "day-2/input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

reports = [list(map(int, line.strip().split(" "))) for line in lines]
total_safe_reports = []


def is_decreasing(data: list) -> bool:
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            continue
        else:
            return False
    
    return True

def is_increasing(data: list) -> bool:
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            continue
        else:
            return False
    
    return True

def absolute_change(data: list) -> bool:
    for i in range(len(data) -1):
        change = abs(data[i] - data[i+1])
        if change >= 1 and change <= 3:
            continue
        else:
            return False
        
    return True

for report in reports:
    same_change = is_decreasing(report) or is_increasing(report)
    abs_change = absolute_change(report)
    total_safe_reports.append(same_change and abs_change)

for index, report in enumerate(reports):
    if total_safe_reports[index] == False:
        for i in range(len(report)):
            new_data = report[:]
            new_data.pop(i)
            same_change = is_decreasing(new_data) or is_increasing(new_data)
            abs_change = absolute_change(new_data)
            if same_change and abs_change:
                total_safe_reports[index] = True
                break

print(total_safe_reports.count(True))
