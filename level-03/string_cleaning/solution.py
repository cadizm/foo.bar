

def answer(chunk, word):
    m = len(word)
    chunks = uninsert(chunk, word, m)

    if not chunks:
        return chunk

    earliest = None
    for c in chunks:
        a = answer(c, word)
        if earliest is None or a < earliest:
            earliest = a

    if earliest is None:
        raise Exception('None for (%s, %s)' % (chunk, word))

    return earliest


def uninsert(chunk, word, m):
    res = set()

    indices = indices_rabin_karp(chunk, word, m)

    for i in indices:
        a = chunk[:i]
        c = chunk[i+m:]

        res.add(a + c)

    return res


def indices_rabin_karp(chunk, word, m):
    res = []
    n = len(chunk)

    h = rabin_fingerprint(word)
    p = rabin_fingerprint(chunk[:m])

    for i in range(n - m + 1):
        if h == p and word == chunk[i:i+m]:
            yield i

        p = rabin_fingerprint(chunk[i+1:i+m+1], prev=p, remove=chunk[i])


def rabin_fingerprint(S, base=101, prev=None, remove=None):
    if prev is None or not S:
        res = 0
        for i, s in enumerate(reversed(S)):
            res += ord(s) * base**i

    else:
        m = len(S) - 1
        add = S[-1]
        res = base * (prev - (ord(remove) * base**m)) + (ord(add) * base**0)

    return res


if __name__ == '__main__':
    chunk = 'lolol'
    word = 'lol'

    assert answer(chunk, word) == 'lo'

    chunk = 'aabb'
    word = 'ab'

    assert answer(chunk, word) == ''

    chunk = "lololololo"
    word = "lol"

    assert answer(chunk, word) == 'looo'

    chunk = "goodgooogoogfogoood"
    word = "goo"

    assert answer(chunk, word) == 'dogfood'
