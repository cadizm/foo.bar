

def answer(minions):
    def f(m):
        t, n, d = [float(v) for v in m]
        return t / (n / d)

    minions = [(i, f(m)) for i,m in enumerate(minions)]
    minions.sort(key=lambda m: m[1])

    return [m[0] for m in minions]


if __name__ == '__main__':
    minions = [[5, 1, 5], [10, 1, 2]]
    assert answer(minions) == [1, 0]

    minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
    assert answer(minions) == [2, 3, 0, 1]
