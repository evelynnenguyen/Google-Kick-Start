def robotPath(prog):
    # print(prog)
    pos = [1, 1]
    for i in prog:
        if i == 'N':
            pos[1] -= 1
        elif i == 'S':
            pos[1] += 1
        elif i == 'E':
            pos[0] += 1
        elif i == 'W':
            pos[0] -= 1
    if pos[0] <= 0:
        pos[0] += 10**9
    if pos[1] <= 0:
        pos[1] += 10**9
    return pos

T = int(input())
for i in range(T):
    prog = input()
    # print(prog)
    li = prog.rfind('(')
    if li == -1:
        pos = robotPath(list(prog))
    else:
        s = []
        prog1 = ''
        for j in range(len(prog)):
            if prog[j] == ')':
                subp = ''
                while s[-1] != '(':
                    subp = subp + s.pop()
                s.pop(-1)
                num = s.pop(-1)
                subp = subp * int(num)
                for m in subp[::-1]:
                    s.append(m)
            else:
                s.append(prog[j])
        pos = robotPath(s)
    print('Case #' + str(i+1) + ': ' + str(pos[0]) + ' ' + str(pos[1]))
