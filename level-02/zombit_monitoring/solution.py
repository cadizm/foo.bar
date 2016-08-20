
def answer(intervals):
    left, right = None, None
    res = 0

    for x,y in sorted(iter(intervals), cmp=stab_cmp):
        # first segment
        if not left and not right:
            left, right = x, y
            res += y - x

        if x < right:
            if y > right:
                res += y - right
                right = y

        else:  # x >= right
            left, right = x, y
            res += y - x

    return res


def stab_cmp(x, y):
    a, b = x[0], y[0]

    if a == b:
        a, b = x[1], y[1]

    return cmp(a, b)


if __name__ == '__main__':
    assert answer([(1, 3), (3, 6)]) == 5
    assert answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]) == 16
