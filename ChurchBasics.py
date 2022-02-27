from Curry import curry


def _numeral(n, g, x):
    if n == 0:
        return x
    else:
        return g(_numeral(n-1, g, x))


numeral = curry(_numeral)
succ = lambda n: n + 1
zero = 0
