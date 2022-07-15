import inspect

from functools import update_wrapper

class Composable:
    def __init__(self, f):
        self.f = f
        update_wrapper(self, f)

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)

    def __getattr__(self, other):
        stack = inspect.stack()[1][0]
        g = stack.f_locals[other]
        fog = lambda *args, **kwds : self.f(g(*args, **kwds))
        return Composable(fog)

if __name__ == "__main__":
    @Composable
    def f(x):
        return x*6

    @Composable
    def g(x):
        return x+3

    class S:
        def __init__(self, a):
            self.a = a

        def f(self, b):
            return self.a * b

    s = S(4)
    h = s.f
    fog = f . g
    print( fog(4) )
    print( (f.h)(8) )

