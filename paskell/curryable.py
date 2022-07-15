from functools import update_wrapper
from inspect import signature, _empty

class Curryable:
    def __init__(self, f):
        self.f = f
        update_wrapper(self, f)
        self.__args, self.__kwds = self.extract_params()

    def extract_params(self):
        sig = signature(self.f)
        params = {**sig.parameters}
        args = [*filter(lambda k:params[k].default == _empty, params)]
        kwds = {k: v for k, v in params.items() if v.default != _empty}
        return args, kwds


    def __call__(self, *args, **kwds):
        # try filling everything in
        remaining_args = self.__args[len(args):]

        # TODO think on how to handle positional args provided via names



# TODO check equality for two partially applied funcs
