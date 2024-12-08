from itertools import permutations

locations = []

with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        _tmp = line.strip()
        locations.append(list(_tmp))

def antinode_cords(prm, dist):
    node_1_cord = node_2_cord = True
    node_1_cord_x = node_1_cord_y = -1
    node_2_cord_x = node_2_cord_y = -1
    node_1, node_2 = prm

    dist_x, dist_y = dist


    node_1_cord_x = node_1[0] + dist_x
    node_1_cord_y = node_1[1] + dist_y

    node_2_cord_x = node_2[0] + (dist_x * -1)
    node_2_cord_y = node_2[1] + (dist_y * -1)

    try:
        if node_1_cord_x >= 0 and node_1_cord_y >= 0 and locations[node_1_cord_x][node_1_cord_y]:
            node_1_cord = [node_1_cord_x, node_1_cord_y]
        else: node_1_cord = False
    except IndexError:
        node_1_cord = False

    try:
        if node_2_cord_x >= 0 and node_2_cord_y >= 0 and locations[node_2_cord_x][node_2_cord_y]:
            node_2_cord = [node_2_cord_x, node_2_cord_y]
        else: node_2_cord = False
    except IndexError:
        node_2_cord = False


    if not node_1_cord and not node_2_cord:
        return False
    else: return node_1_cord, node_2_cord


freq: dict[str:list[list]] = {}
antinodes = []

for x in range(0,len(locations)):
    location = locations[x]
    for i in range(0,len(location)):
        if location[i] == "." or location[i] == "#": continue
        if location[i] in freq: freq[location[i]].append([x, i])
        else: freq[location[i]] = [[x,i]]

for f in freq:
    permutation = permutations(freq[f], 2)
    for perm in permutation:
        antinodes.append(str(list(perm[0])))
        antinodes.append(str(list(perm[1])))
        dist_x = perm[0][0] - perm[1][0]
        dist_y = perm[0][1] - perm[1][1]
        distance = (dist_x, dist_y)
        # _tmp = antinode_cords(perm, distance)
        # for i in _tmp:
        #     try:
        #         if i and locations[i[0]][i[1]]: antinodes.append(str(i))
        #     except IndexError:
        #         pass
        cont = True
        while cont:
            _tmp = antinode_cords(perm, distance)
            if not _tmp: break
            for i in _tmp:
                    if i : antinodes.append(str(i))
            distance = (distance[0] + dist_x, distance[1] + dist_y)

print(len(set(antinodes)))