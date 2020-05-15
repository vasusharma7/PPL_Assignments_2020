#l is the left bank and r is the right bank of river
#Goal is to move everyone from right to left bank i.e. empty the right list
from itertools import permutations
logs = []
prev_logs = []
def game_over(bank):
    if len(bank) == 2 and ('goat' in bank and 'grass' in bank):
        return True
    if len(bank) == 2 and ('goat' in bank and 'tiger' in bank):
        return True
    return False
def solve(r):
    global prev_logs
    global logs
    logs = []
    l = []
    while r != []:
        prev = ""
        for i in range(len(r)):
            temp = r.copy()
            if not r[i] == prev:
                prev = r[i]
                l.append(temp[i])
                r.pop(r.index(temp[i]))
            if game_over(r):
                prev = ""
                r = [l.pop(-1)] + r
            else:
                logs.append("Take " + temp[i] + " from right to left")
                # print(logs[-1])
                break
        if r == []:
            break
        if len(l) != 1 and game_over(l):
            for j in range(len(l)):
                temp = l.copy()
                if not l[j] == prev:
                    prev = l[j]
                    r.append(temp[j])
                    logs.append("Take " + temp[j] + " from left to right")
                    # print(logs[-1])
                    break
    if logs in prev_logs:
        return
    dir = [sp.split()[-1] for sp in logs]
    for i in range(len(logs)):
        print(logs[i])
        try:
            if dir[i] == dir[i+1]:
                print("Move to the other side of the bank")
        except IndexError:
            pass
    prev_logs.append(logs)

for i in permutations(["goat","tiger","grass"]):
    solve(list(i))
    print()