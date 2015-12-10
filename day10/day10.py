from itertools import groupby
import sys


def look_and_say(s):
    next = []
    for char, countlist in groupby(s):
        next.append(str(len(list(countlist))))
        next.append(char)
    return "".join(next)


def main(start, iterations):
    out = start
    for x in range(0, iterations):
        out = look_and_say(out)
    print(len(out))

#call with input string and number of iterations
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
