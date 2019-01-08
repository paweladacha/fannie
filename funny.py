def fan(fs,para):
    for f in fs:
        yield f(para)

def pin(fs,para):
    w = para
    for f in fs:
        w = f(w)
    return w

argph = type("ArgPlaceholder",
        (object,),
        {'__slots__':[],
            '__repr__':lambda s:'{v}',
            '__call__':lambda s:s,})()

class partial(object):
    def __init__(self,func,*args,**kwargs):
        self.f = func
        self.a = list(args)
        self.kw = kwargs

    def __call__(self,*a,**kw):
        # ai = list(reversed(a))  
        args = self.a[:]
        ph_inds = [ x for x in range(len(args)) if args[x] is argph]
        ai = iter(a)
        for ind,val in zip(ph_inds, ai):
            args[ind] = val
        args.extend(ai)
        kw = {**self.kw, **kw}
        return self.f(*args,**kw)

    def __repr__(self):
        s = self ; psep = ', '
        args = ['{}'.format(x) for x in s.a]
        kwargs=['{k}={v}'.format(k=k,v=v) for k,v in s.kw.items()]
        params = psep.join(args + kwargs)
        return '{fn}({p})'.format(p=params,
            fn = getattr(s.f,'__name__','')
                or getattr(type(s.f),'__name__','')
                or getattr(s.f, '__qualname__', str(s.f)) )
