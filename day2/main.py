reports = []
with (open('puzzle_input.txt', 'r') as puzzle_input):
    for line in puzzle_input:
        level = []
        for i in line.split():
            level.append(int(i))
        reports.append(level)

def check_safe(check_level):
    inc, dec, same = False

    for i in range(0, len(check_level)-1):
        diff = check_level[i] - check_level[i+1]
        if diff > 0: inc = True
        if diff < 0: dec = True
        if diff == 0: same = True

        if (abs(diff) > 3) or same or (inc and dec):
            return False
    return True

def dampener(check_level):
    for i in range(0, len(check_level)):
        damp_level = check_level.copy()
        damp_level.pop(i)
        if check_safe(damp_level):
            return True

### Processing ###
safe_count = 0
dampener_safe_count = 0

for report in reports:
    if check_safe(report): safe_count += 1
    elif dampener(report): dampener_safe_count += 1

print(safe_count + dampener_safe_count)
