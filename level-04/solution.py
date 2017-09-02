
import sys
from itertools import permutations


def answer(x, y, n):
    count = 0
    L = range(n)
    for p in permutations(L):
        if check_left(p, x) and check_right(p, y):
            count += 1

    return count


def check_left(L, n):
    count = 0
    seen = -1
    for e in L:
        if e > seen:
            count += 1
            seen = e
        if count > n:
            return False

    return True if count == n else False


def check_right(L, n):
    return check_left(reversed(L), n)


if __name__ == '__main__':
    SINGLE_ANSWER = True

    if SINGLE_ANSWER:

        x = 1
        y = 11
        n = 12

        print "(%d, %d, %d) => %d" % (x, y, n, answer(x, y, n))

    else:

        for n in range(3, 11+1):
            for x in range(1, n+1):
                for y in range(1, n+1):
                    print "(%d, %d, %d) => %d" % (x, y, n, answer(x, y, n))



#
#
# (1, 2, 3) => 1
# (1, 3, 4) => 3 = 1 + 2
# (1, 4, 5) => 6 = 3 + 3
# (1, 5, 6) => 10 = 6 + 4
# (1, 6, 7) => 15 = 10 + 5
# (1, 7, 8) => 21 = 15 + 6
# (1, 8, 9) => 28 = 21 + 7
# (1, 9, 10) => 36 = 28 + 8
# (1, 10, 11) => 45 = 36 + 9
# (1, 11, 12) => 55 = 45 + 10
#
