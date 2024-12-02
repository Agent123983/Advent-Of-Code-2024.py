
left_list = []
right_list = []
diff_list = []
with open('test_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        # print(line)
        space_index = line.find(" ")
        left_list.append(int(line[:space_index]))
        # print(int(line[:space_index]))
        right_list.append(int(line[space_index+3:]))

# Part 1
# left_list.sort()
# right_list.sort()
# for i in range(0,len(left_list)):
#     diff_list.append(abs(left_list[i]-right_list[i]))
#
# sum = 0
# for num in diff_list:
#     sum = sum+num
#
# print(sum)

# Part 2
value = 0
for i in left_list:
    value += i * (right_list.count(i))

print(value)