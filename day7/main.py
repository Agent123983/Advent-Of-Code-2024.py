from itertools import permutations, product
from operator import indexOf

equations = []

with open('puzzle_input.txt', 'r') as puzzle_input:
    for line in puzzle_input:
        line.strip()
        ans = line.split(':')
        ans[1] = ans[1].split()
        equations.append(ans)


def solve(ans, list):

    for ops in product(['*','+', '||'], repeat=len(list)-1):
        expr = str(list[0])
        for i in range(1, len(list)):
            if ops[0] == '||' and len(ops) == 1:
                expr = expr + str(list[i])
            elif ops[0] == '||' and len(ops) > 1 and i == 1:
                expr = str(eval(expr))
                expr = expr +str(list[i])
            elif ops[i-1] == '||':
                # fi = expr.rfind('(') if expr.rfind('(') != 0 and ops[-1] != '||' else None
                # li = expr.rfind(')') if fi is not None else None
                # expr = str(eval(expr[fi:li]))
                expr = str(eval(expr))
                expr = expr + str(list[i])
            else: expr += ops[i-1] + str(list[i])
            expr = '(' + expr + ')'
        try:
            if eval(expr) == int(ans):
                return int(ans)
        except ZeroDivisionError:
            pass
    return 0


### Processing ###
return_list = []
return_sum = 0
for eq in equations:
    return_sum += solve(eq[0], eq[1])


print(return_sum)

