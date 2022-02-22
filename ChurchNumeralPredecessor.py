from Curry import curry


def numeral(n, g, x):
    if n == 0:
        return x
    else:
        return g(numeral(n-1, g, x))


pnumeral = curry(numeral)
succ = lambda n: n + 1
zero = 0

print(pnumeral(4)(succ)(zero))

f = curry(lambda a, b, c, d: a(b)(b(c))(c))
h = curry(lambda a, b, c: c)
pred = curry(lambda n, g, x: n(f)(h)(g)(x)(None))

print(pred(pnumeral(5))(succ)(zero))
