# --- Day 5: Print Queue ---

with open("day-5/input.txt") as file:
    lines = file.readlines()
    order_rules = [list(map(int, line)) for line in [line.strip().split("|") for line in lines if line.find("|") != -1]]
    page_update_numbers = [list(map(int, line)) for line in [line.strip().split(",") for line in lines if line.find(",") != -1]]

page_ordering_rules: dict[int, set] = {}

for order in order_rules:
    if order[0] in page_ordering_rules.keys():
        page_ordering_rules[order[0]].add(order[1])
    else:
        page_ordering_rules[order[0]] = {order[1]}
# print(page_ordering_rules)

results = [True for i in range(len(page_update_numbers))]

for i, page_update in enumerate(page_update_numbers):
    break_outer = False
    for page_number in page_update:
        if break_outer:
            break
        for main, page_order in page_ordering_rules.items():
            if page_number in page_order and main in page_update:
                main_index = page_update.index(main)
                page_number_index = page_update.index(page_number)
                if main_index > page_number_index:
                    results[i] = False
                    break_outer = True
                    break

total = 0
incorrectly_ordered_page_numbers = []
for x, y in zip(results, page_update_numbers):
    if x:
        total += y[(len(y) // 2)]
    else:
        incorrectly_ordered_page_numbers.append(y)

# print(total)

ordered_results = []
for i, page_update in enumerate(incorrectly_ordered_page_numbers):
    x = 0
    while x < len(page_update):
        page_number = page_update[x]
        break_outer = False
        for main, page_order in page_ordering_rules.items():
            if page_number in page_order and main in page_update:
                main_index = page_update.index(main)
                page_number_index = page_update.index(page_number)
                if main_index > page_number_index:
                    temp = page_update[main_index]
                    page_update[main_index] = page_update[page_number_index]                    
                    page_update[page_number_index] = temp
                    x -= 1
                    break_outer = True
                    break
        if break_outer:
            continue
        else:        
            x += 1

    ordered_results.append(page_update)

total = sum([item[len(item)//2] for item in ordered_results])
print(total)