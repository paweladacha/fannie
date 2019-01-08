''' fannie - extended partial function '''

from . import funny
from .funny import *
    
try:
    from . import predefined
    pre = predefined
    agg = pre.agg
    del predefined
except (ImportError):
    print('fannie: failed to import .predefined\nA true journey awaits you, Explorer.')


shortcuts = dict(\
    p = partial,
    v = pin,
    a = fan,
    m = agg.map_,
    f = agg.filter_,
    x = argph, )

modules = dict(
    funny = funny,
    predefined = pre,)

del partial,pin,fan,argph

locals().update(shortcuts)

__doc__ += '\nModule contents'
__doc__+= '\n'.join(['{}: {}'.format(k,v) for k,v in shortcuts.items()])