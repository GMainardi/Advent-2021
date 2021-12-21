class Dice:
    curr = 1
    rolls = 0

    def __init__(self) -> None:
        self.curr = 1
        self.rolls = 0

    def roll(self):
        roll = 3 * self.curr + 3
        self.curr += 3
        self.rolls += 3
        return roll

def cal_pos(pos, row):
    return (pos + row - 1) % 10 + 1

players = [int(line.strip().split(' ')[-1]) for line in open('input.txt', 'r')]
scores = [0,0]
i = 0
dice = Dice()

while scores[0] < 1000 and scores[1] < 1000:
    curr = i % 2
    row = dice.roll()
    players[curr] = cal_pos(players[curr], row)
    scores[curr] += players[curr]
    i += 1

loser = scores[0] if scores[0] < 1000 else scores[1]
print(loser * dice.jogadas)