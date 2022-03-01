from ChurchBasics import *

nil = curry(lambda f, g: g)
cons = curry(lambda a, l, f, g: f(a)(l(f)(g)))


def py2church(arr):
    if not arr:
        return nil
    else:
        return cons(numeral(arr[0]))(py2church(arr[1:]))


length = curry(lambda l, f: l(lambda u: f))
summ = curry(lambda l, f: l(lambda u: u(f)))
product = lambda l: l(identity)
tower = lambda l: l(curry(lambda u, v: v(u)))(identity)
reverse = lambda l: l(curry(lambda u, v, f, g: v(f)(f(u)(g))))(curry(lambda f, g: g))
reverse_tower = lambda l: tower(reverse(l))
fst = curry(lambda b, c: b)
snd = curry(lambda b, c: c)
nil_list = curry(lambda f, g: g)
head = curry(lambda l, d: l(curry(lambda u, v: u))(d))
tail = curry(lambda l, d, f, g: l(curry(lambda u, v, a: a(f(u)(v(fst)))(v(fst))))
                                       (lambda a: a(g)(d))(snd))
tail_sum = lambda l: summ(tail(l)(identity))
nth = curry(lambda n, l: head(n(lambda l2: tail(l2)(nil))(l))(identity))
second = nth(numeral(2))


test_arrays = [
    [1, 2, 3],
    [2, 4, 1],
    [3, 2, 2]
]
test_functions = [
    ("length", length),
    ("sum", summ),
    ("product", product),
    ("tower", tower),
    ("reverse tower", reverse_tower),
    ("tail sum", tail_sum),
    ("2th", second)
]


def main():
    for arr in test_arrays:
        print(f"array {arr}")
        print("--------")
        for name, func in test_functions:
            print(f"{name} is {func(py2church(arr))(succ)(zero)}")
        print()


main()
