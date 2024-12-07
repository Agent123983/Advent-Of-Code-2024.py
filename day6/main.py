map = []
with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        map.append(list(line.strip()))

og_start = []

for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == '^': og_start= [i,j]

def move(pos, dir, obs = None, steps = None):
    x = y =0
    next_dir = None
    try:
        match dir:
            case 'up':
                x = -1
                y = 0
                next_dir = 'right'
            case 'right':
                x = 0
                y = 1
                next_dir = 'down'
            case 'down':
                x = 1
                y = 0
                next_dir = 'left'
            case 'left':
                x = 0
                y = -1
                next_dir = 'up'

        while map[pos[0] + x][pos[1] + y] != '#':
            if pos[0] < 0 or pos[1] < 0: raise IndexError
            if [pos[0]+x, pos[1]+y] == obs:
                return pos, next_dir, True
            pos[0] += x
            pos[1] += y
            if steps: steps.append(str([pos[0], pos[1]]))
        return pos, next_dir, False

    except IndexError as e:
        return pos, 'Out_Of_Bounds', False

def part_1():
    p1_steps = []
    direction = 'up'
    start = og_start.copy()
    while direction != 'Out_Of_Bounds':
        start, direction, obj_hit = move(start, direction, p1_steps)
    print(len(set(p1_steps)))


def part_2():
    counter = 0
    invalid = ['#', '^']
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            direction = 'up'
            start = og_start.copy()
            if map[i][j] not in invalid:
                obj = [i,j]
            else: continue
            repeats = 10
            steps = ['*']
            up_repeat = \
            down_repeat = \
            right_repeat = \
            left_repeat = False

            while direction != 'Out_Of_Bounds':
                current_step = [direction]
                start, direction, obj_hit = move(start, direction, obj, current_step)
                match current_step[0]:
                    case 'up':
                        if steps.count(current_step) >= repeats: up_repeat = True
                    case 'right':
                        if steps.count(current_step) >= repeats: right_repeat = True
                    case 'down':
                        if steps.count(current_step) >= repeats: down_repeat = True
                    case 'left':
                        if steps.count(current_step) >= repeats: left_repeat = True

                steps.append(current_step)
                if up_repeat & down_repeat & right_repeat & left_repeat:
                    if obj == start: break
                    counter += 1
                    break

    print(counter-1) #I have no idea anymore




if __name__ == '__main__':
    # part_1()
    part_2()