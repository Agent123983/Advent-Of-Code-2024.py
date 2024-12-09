disk_map = []
with open("puzzle_input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        _tmp = line.strip()
        disk_map = list(_tmp)

print("Building Disk")
disk = []
id_index = 0
file_location = [] #ID_index:Size
free_space = [] #Start_Index:Size

for i in range(0, len(disk_map)):
    if i % 2 == 0:
        for j in range(0,int(disk_map[i])):
            disk.append(id_index)
        file_location.append([id_index,int(disk_map[i])])
        id_index += 1
    else:
        free_space.append([len(disk), int(disk_map[i])])
        for j in range(0,int(disk_map[i])):
            disk.append(".")

# print(disk)
# print(file_location)
# print(free_space)

# print("Starting Ordering")
# for i in range(0, len(disk)):
#     try:
#         free_index = disk.index(".")
#         disk.insert(disk.index("."), disk.pop(-1))
#         disk.pop(free_index+1)
#     except ValueError:
#         pass
#     except IndexError:
#         pass

def free_space_check():
    _tmp_list = []
    _tmp = 0
    for i in range(0, len(disk)):
        if _tmp >0:
            _tmp -= 1
        else:
            try:
                while disk[i + _tmp] == ".":
                    _tmp += 1
            except IndexError:
                pass
            if _tmp == 0:
                pass
            else:
                _tmp_list.append([i, _tmp])
                _tmp -= 1
    return _tmp_list

print("Started Ordering")
for i in range(0, len(file_location))[::-1]:
    try:
        for j in free_space:
            if file_location[i][1] <= j[1] and j[0] < disk.index(file_location[i][0]):
                free_index_c = 0
                pop_index = disk.index(file_location[i][0])
                for z in range(0,file_location[i][1]):
                    free_index_c += 1
                    disk.insert(j[0], disk.pop(pop_index))
                    disk.pop(j[0] + free_index_c)
                for z in range(0,free_index_c):
                    disk.insert(pop_index, '.')
                break

    except ValueError:
        pass
    except IndexError:
        pass
    free_space = free_space_check()



check_sum = 0
print("Started Check Sum")
for i in range(0, len(disk)):
    if type(disk[i]) == int:
        check_sum += i * disk[i]


print(check_sum)