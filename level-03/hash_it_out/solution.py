
def answer(digest):
    return unhash(digest)


def hash_(message):
    digest = []

    for i in range(len(message)):
        a = message[i]
        b = message[i - 1] if i > 0 else 0
        digest.append(((129 * a) ^ b) % 256)

    return digest


def unhash(digest):
    res = []

    for i in range(16):
        b = res[-1] if i > 0 else 0
        a = digest[i] ^ b

        pool = [
            a % 256,
            abs(128 - (a % 256)),
            (a % 256) + 128,
        ]

        for k in pool:
            if hash_(res + [k]) == digest[:i + 1]:
                res.append(k)
                continue

    return res


if __name__ == '__main__':
    assert hash_([1, 129]) == [129, 0]

    m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    d = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]

    assert hash_(m) == d
    assert unhash(hash_(m)) == m
    assert answer(d) == m

    m = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    d = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]

    assert hash_(m) == d
    assert unhash(hash_(m)) == m
    assert answer(d) == m

    m = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    d = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]

    assert hash_(m) == d
    assert unhash(hash_(m)) == m
    assert answer(d) == m

    import random
    random.seed()

    for i in range(10000):
        m = [random.randint(0, 255) for _ in range(16)]
        assert unhash(hash_(m)) == m
