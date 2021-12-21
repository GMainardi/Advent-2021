import itertools

def sum_tup(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

rows = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]

mem = {}
def count_wins(P1, S1, P2, S2, P1_turn):

    if (P1, S1, P2, S2, P1_turn) in mem.keys():
        return mem[(P1, S1, P2, S2, P1_turn)]

    if S1 >= 21:
        mem[(P1, S1, P2, S2, P1_turn)] = (1,0)
        return mem[(P1, S1, P2, S2, P1_turn)]
    elif S2 >= 21:
        mem[(P1, S1, P2, S2, P1_turn)] = (0,1)
        return mem[(P1, S1, P2, S2, P1_turn)]

    mem[(P1, S1, P2, S2, P1_turn)] = (0,0)
    for row in rows:
        if P1_turn:
            new_pos = (P1 + row - 1) % 10 + 1
            mem[(P1, S1, P2, S2, P1_turn)] = sum_tup(mem[(P1, S1, P2, S2, P1_turn)], count_wins(new_pos, S1 + new_pos, P2, S2, False))
        else:
            new_pos = (P2 + row - 1) % 10 + 1
            mem[(P1, S1, P2, S2, P1_turn)] = sum_tup(mem[(P1, S1, P2, S2, P1_turn)], count_wins(P1, S1, new_pos, S2 + new_pos, True))
    return mem[(P1, S1, P2, S2, P1_turn)]


players = [int(line.strip().split(' ')[-1]) for line in open('input.txt', 'r')]

print(max(count_wins(players[0], 0, players[1], 0, True)))