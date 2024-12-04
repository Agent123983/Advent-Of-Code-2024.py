rows = []
xmas_count =ver = fo = ba = diagonal = 0


with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        col = list(line)
        col.pop(col.index('\n'))
        rows.append(col)

def forward(rows, x, y):
    try:
        if rows[x][y] == 'X':
            if rows[x][y+1] == 'M':
                if rows[x][y+2] == 'A':
                    if rows[x][y+3] == 'S':
                        return True
    except IndexError:
        pass

def backward(rows, x, y):
    if y in [0,1,2]:
        return False
    try:
        if rows[x][y] == 'X':
            if rows[x][y - 1] == 'M':
                if rows[x][y - 2] == 'A':
                    if rows[x][y - 3] == 'S':
                        return True
    except IndexError:
        pass

def d_vertical(rows, x, y):
    try:
        if rows[x][y] == 'X':
            if rows[x + 1][y] == 'M':
                if rows[x + 2][y] == 'A':
                    if rows[x + 3][y] == 'S':
                        return True
    except IndexError:
        pass

def u_vertical(rows, x, y):
    if x in [0,1,2]:
        return False
    try:
        if rows[x][y] == 'X':
            if rows[x - 1][y] == 'M':
                if rows[x - 2][y] == 'A':
                    if rows[x - 3][y] == 'S':
                        return True
    except IndexError:
        pass


def fu_diagonal(rows, x, y):
    if x in [0,1,2]:
        return False
    try:
        if rows[x][y] == 'X':
            if rows[x - 1][y + 1] == 'M':
                if rows[x - 2][y + 2] == 'A':
                    if rows[x - 3][y + 3] == 'S':
                        return True
    except IndexError:
        pass

def bu_diagonal(rows, x, y):
    if x in [0,1,2] or y in [0,1,2]:
        return False
    try:
        if rows[x][y] == 'X':
            if rows[x - 1][y - 1] == 'M':
                if rows[x - 2][y - 2] == 'A':
                    if rows[x - 3][y - 3] == 'S':
                        return True
    except IndexError:
        pass

def fd_diagonal(rows, x, y):
    try:
        if rows[x][y] == 'X':
            if rows[x+1][y + 1] == 'M':
                if rows[x + 2][y + 2] == 'A':
                    if rows[x + 3][y + 3] == 'S':
                        return True
    except IndexError:
        pass

def bd_diagonal(rows, x, y):
    if y in [0,1,2]:
        return False
    try:
        if rows[x][y] == 'X':
            if rows[x + 1][y - 1] == 'M':
                if rows[x + 2][y - 2] == 'A':
                    if rows[x + 3][y - 3] == 'S':
                        return True
    except IndexError:
        pass


def x_mas(rows, x, y):
    c1 = c2 = False
    try:
        if x == 0 or y == 0: return False
        if rows[x][y] == 'A':
            c1_values = ['M', 'S']
            if rows[x-1][y-1] in c1_values:
                c1_values.remove(rows[x-1][y-1])
                if rows[x+1][y+1] in c1_values:
                    c1 = True
            c2_values = ['M', 'S']
            if rows[x+1][y-1] in c2_values:
                c2_values.remove(rows[x+1][y-1])
                if rows[x-1][y+1] in c2_values:
                    c2 = True
        if c1 and c2: return True
        else: return False
    except IndexError:
        pass


### Processing ###
# for i in range(0,len(rows)):
#     for col in range(0,len(rows[i])):
#         if forward(rows, i, col): xmas_count += 1
#         if backward(rows, i, col): xmas_count += 1
#         if d_vertical(rows, i, col): xmas_count += 1
#         if u_vertical(rows, i, col): xmas_count += 1
#         if fu_diagonal(rows, i, col): xmas_count += 1
#         if bu_diagonal(rows, i, col): xmas_count += 1
#         if fd_diagonal(rows, i, col): xmas_count += 1
#         if bd_diagonal(rows, i, col): xmas_count += 1

for i in range(0,len(rows)):
    for col in range(0,len(rows[i])):
        if x_mas(rows, i, col): xmas_count += 1


print(xmas_count)
