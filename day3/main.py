import re

part_1_regex = r"mul\(\d*,\d*\)"
part_2_regex = r"(do\(\))|(don\'t\(\))|(mul\(\d*,\d*\))"
sum_1 = sum_2 = 0

with (open('puzzle_input.txt', 'r') as puzzle_input):
    multiples = re.finditer(part_1_regex, puzzle_input.read(), re.MULTILINE)
with (open('puzzle_input.txt', 'r') as puzzle_input):
    matches = re.finditer(part_2_regex, puzzle_input.read(), re.MULTILINE)


def mul(num1, num2):
    return num1 * num2

### Processing ###
for matchNum, match_box in enumerate(multiples, start=1):
    func = str(match_box.group())
    sum_1 += eval(func)

skip = False
for matchNum_2, match_box_2 in enumerate(matches, start=1):
    match_value = str(match_box_2.group())
    if not skip:
        match match_value:
            case 'do()': skip = False
            case 'don\'t()': skip = True
            case _ :sum_2 += eval(match_value)
    elif match_value == 'do()': skip = False
print(sum_1,sum_2)