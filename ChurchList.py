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


test_arrays = [
    [1, 2, 3],
    [2, 4, 1],
    [3, 2, 2]
]
test_functions = [
    ("length", length),
    ("sum", summ),
    ("product", product),
    ("tower", tower)
]


def main():
    for arr in test_arrays:
        print(f"array {arr}")
        print("--------")
        for name, func in test_functions:
            print(f"{name} is {func(py2church(arr))(succ)(zero)}")
        print()


main()
