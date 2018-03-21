import types
import importlib


module = importlib.import_module('Tshirt')

def func(*args):
    print (len(args))
    for arg in args:
        for a in arg.__dict__.values():
            if types(a) == types.ModuleType:
                print (a)

func(module)
