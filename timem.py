from time import time
import sys

def sizeof(obj):
    return sum(map(sys.getsizeof, explore(obj, set())))

def explore(obj, memo):
    loc = id(obj)

    if loc not in memo:
        memo.add(loc)
        yield obj

        try:
            slots = obj.__slots__
        except AttributeError:
            pass
        else:
            for name in slots:
                try:
                    attr = getattr(obj, name)
                except AttributeError:
                    pass
                else:
                    yield from explore(attr, memo)

        try:
            attrs = obj.__dict__
        except AttributeError:
            pass
        else:
            yield from explore(attrs, memo)

        for name in 'keys', 'values', '__iter__':
            try:
                attr = getattr(obj, name)
            except AttributeError:
                pass
            else:
                for item in attr():
                    yield from explore(item, memo)

class Timem(object):
    last_time = 0
    start_time = time()
    last_memory_usage = 0
    total_memory_usage = 0

def timeit(method):

    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        Timem.last_time = te - ts
        return result

    return timed

def memit(alignment):

    Timem.last_memory_usage = sizeof(alignment)
    Timem.total_memory_usage += Timem.last_memory_usage

