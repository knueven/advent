import re
import json


def part1(inp):
    return sum(map(int, re.findall("-?[0-9]+", inp)))


def part2(inp):
    if isinstance(inp, type(0)):
        return inp
    if isinstance(inp, dict) and not 'red' in inp.values():
        return sum(map(part2, inp.values()))
    if isinstance(inp, list):
        return sum(map(part2, inp))
    return 0

if __name__ == "__main__":
    inp = open("day12input.txt").read()
    print("part 1: {0}".format(part1(inp)))
    print("part 2: {0}".format(part2(json.loads(inp))))
