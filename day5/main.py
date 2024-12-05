import math

page_order_rules = []
page_updates = []
correct_sum = 0
incorrect_sum = 0

with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        try:
            if line.index("|") != -1:
                page_order_rules.append(line.strip().split("|"))
        except ValueError:
            pass
with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        try:
            if line.index(",") != -1:
                page_updates.append(line.strip().split(","))
        except ValueError:
            pass


def breaks_rules(update):
    try:
        for rule in page_order_rules:
            try:
                if update.index(rule[0]) > update.index(rule[1]):
                    return True
                else: continue
            except ValueError:
                continue
        return False
    except:
        pass


def update_rules(update) -> list:
    for rule in page_order_rules:
        try:
            if update.index(rule[0]) > update.index(rule[1]):
                update.insert(0, update.pop(update.index(rule[0])))
                return update
        except ValueError:
            pass

### Processing ###
correct_updates = page_updates.copy()
incorrect_updates = []
for i in range(0,len(page_updates)):
    current_update = page_updates[i]
    if breaks_rules(current_update):
        correct_updates.pop(correct_updates.index(current_update))
        incorrect_updates.append(current_update)

for update in correct_updates:
    correct_sum += int(update[math.ceil(len(update)/2)-1])

print("Part 1:", correct_sum)


for update in incorrect_updates:
    while breaks_rules(update):
        update = update_rules(update)
        # print(update)

for update in incorrect_updates:
    incorrect_sum += int(update[math.ceil(len(update)/2)-1])

print("Part 2:", incorrect_sum)
