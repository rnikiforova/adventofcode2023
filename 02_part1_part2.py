import re
from functools import reduce
from operator import mul

game_pat = re.compile(r"Game (?P<game_id>\d+): ")


def parse_line(line):
    m = game_pat.match(line)
    game_id = int(m.group("game_id"))
    pos_colon = m.span()[-1]
    sets = line[pos_colon:].split(";")
    return sets, game_id


def part2(path):
    with open(path) as f:
        total = 0
        for line in f:
            max_per_color = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            sets, _ = parse_line(line)
            for set_ in sets:
                for item in set_.split(","):
                    num, color = item.strip().split(" ")
                    max_per_color[color] = max(max_per_color[color], int(num))
            total += reduce(mul, max_per_color.values())
        return total


def part1():
    constraints = {"red": 12, "green": 13, "blue": 14}

    with open(path) as f:
        total = 0
        for line in f:
            possible = True
            sets, game_id = parse_line(line)
            for set_ in sets:
                items = set_.split(",")
                for item in items:
                    num, color = item.strip().split(" ")
                    if int(num) > constraints[color]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                total += int(game_id)
        return total


if __name__ == "__main__":
    path = "data/02_part1_example.txt"
    assert part1() == 8
    assert part2(path) == 2286
