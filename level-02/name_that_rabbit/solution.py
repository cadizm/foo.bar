
def answer(names):
    table = {name: score(name) for name in names}
    S = sorted(table.items(), cmp=name_cmp, reverse=True)

    return [x[0] for x in S]  # only want names, not scores


def score(name):
    def val(letter):
        return ord(letter) - ord('a') + 1

    return sum([val(letter) for letter in name])


def name_cmp(x, y):
    name1, score1 = x
    name2, score2 = y

    if score1 != score2:
        return cmp(score1, score2)

    return cmp(name1, name2)


if __name__ == '__main__':
    assert score('annie') == 43
    assert score('earz') == 50

    assert score('al') == 13
    assert score('cj') == 13

    assert answer(['al', 'cj']) == ['cj', 'al']

    assert answer(["annie", "bonnie", "liz"]) == ["bonnie", "liz", "annie"]
    assert answer(["abcdefg", "vi"]) == ["vi", "abcdefg"]
