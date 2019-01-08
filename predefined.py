__all__ = ['agg']
import fannie as fx


class agg(object):
    ''' Map and filter versions with built-in aggregation
    i.e. map_(func,data) == list(map(func,data)) '''

    def filter_(f, iterable=None, cls=list):
        fif = fx.p(fx.v, [fx.p(filter, f), cls])
        if iterable:
            return fif(iterable)
        return fif

    def map_(f, *iterables, cls=list):
        mf = fx.p(fx.v, [fx.p(map, f), cls])
        if iterables:
            return mf(iterables)
        return mf
