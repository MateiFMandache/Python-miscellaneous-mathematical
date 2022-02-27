from Curry import curry
from ChurchBasics import numeral, succ, zero

f = curry(lambda a, b, c, d: a(b)(b(c))(c))
h = curry(lambda a, b, c: c)
pred = curry(lambda n, g, x: n(f)(h)(g)(x)(None))

print(pred(numeral(5))(succ)(zero))
