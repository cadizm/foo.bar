
def answer(x):
    if x < 10:
        return x

    res = 0

    while x > 9:
        res += x % 10
        x /= 10

    res += x

    return answer(res)


def _test1():
    assert answer(13) == 4

def _test2():
    assert answer(1235) == 2


if __name__ == '__main__':
    _test1()
    _test2()
