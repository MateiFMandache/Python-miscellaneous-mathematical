from inspect import getfullargspec


def curry(func):
    """This doesn't work"""
    args, *_ = getfullargspec(func)
    context = {"func0": func}
    for i in range(len(args)-1):
        exec(
            f"def new_func(*new_args):\n"
            f"    return lambda a: func{i}(*new_args, a)\n"
            f"func{i+1} = new_func",
            context
        )
    return eval(f"func{len(args)-1}", context)
