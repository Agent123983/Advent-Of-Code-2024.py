topology = []

with open('test_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        _tmp = line.strip()
        topology.append(list(map(int, _tmp)))

def check_route(cords):
    _x, _y = cords
    up = down = left = right = False
    loc = topology[_x][_y]
    next_move = []
    while loc != 9:
        try:
            if topology[_x-1][_y] == loc +1: # Up
                up = True
            if topology[_x+1][_y] == loc +1: # Down
                down = True
            if topology[_x][_y-1] == loc +1: # Left
                left = True
            if topology[_x][_y+1] == loc +1: # Right
                right = True
        except IndexError:
            break

        if sum([up, down, left, right]) > 1:
            print('multiple_paths')
            break
        elif sum([up, down, left, right]) == 0:
            break
        else:
            return 1



potential_trailhead = []
# Get potential trailheads
for x in range(0, len(topology)):
    for y in range(0, len(topology[x])):
        if topology[x][y] == 0:
            potential_trailhead.append([x,y])

trailhead_score_list = []
for x in range(0, len(potential_trailhead)):
    trailhead_score_list.append(potential_trailhead[x]) if check_route(potential_trailhead[x]) == 1 else None

print(trailhead_score_list)