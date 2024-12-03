import re
regex = r"(do\(\))|(don\'t\(\))|(mul\(\d*,\d*\))"



multiples = []
with (open('puzzle_input.txt', 'r') as puzzle_input):
    matches = re.finditer(regex, puzzle_input.read(), re.MULTILINE)


def mul(num1, num2):
    return num1 * num2

sum = 0

# for list in multiples:
#     for func in list:
#         sum += eval(func)
#
# print(sum)
# for matchNum, match_box in enumerate(matches, start=1):
#     print(match_box.group())

skip = False
for matchNum, match_box in enumerate(matches, start=1):
    match_value = str(match_box.group())
    if not skip:
        match match_value:
            case 'do()': skip = False
            case 'don\'t()': skip = True
            case _ :sum += eval(match_value)
    elif match_box.group() == 'do()': skip = False

print(sum)