import sys
import random


def gen_match(players, depth):
    if type(players) is str:
        return '*' * depth + f' {players}\n'
    
    text = '*' * depth + f' Nivel #{depth}\n'
    text += gen_match(players[0], depth+1)
    text += gen_match(players[1], depth+1)
    return text


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: generate_match.py <input_file> <output_file>')
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    players = []
    with open(input_file) as fd:
        for addr in fd.readlines():
            addr = addr.lstrip('*').strip()
            if not addr:
                continue
            players.append(addr)

    players = list(set(players))
    random.shuffle(players)

    print('Number of players:', len(players))
    while len(players) > 1:
        match = []
        while len(players) > 1:
            p1 = players.pop(0)
            p2 = players.pop(0)
            match.append((p1, p2))
        players = players + match

    with open(output_file, 'w') as fd:
        fd.write(gen_match(players[0], 1))
