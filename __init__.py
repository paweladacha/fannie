''' 2do here 

-> shortcuts
-> modules:
    name for filters '''

from .funny import *
from .filters import *
from . import conds

try:
    from . import dirtyaddons
    dirt = dirtyaddons
    del dirtyaddons
except (ImportError):
    print('fannie: failed to import .dirtyaddons\nno rough play tonight')

try:
    from . import relind
    ri = relind
    del relind
except (ImportError):
    print('fannie: failed to import .relind\nno new relations tonight')
    
try:
    from . import predefined
    pre = predefined
    agg = pre.agg
    del predefined
except (ImportError):
    print('fannie: failed to import .predefined\nA true journey awaits you tonight, Explorer.')


# shortcuts
# comments: _______________________@
#
# --- partial
# skewed -> raczej b jak biased;
# a s jak star (ktorego nie ma a robi tyle co f(g,x)->g(*x))
# czyli taki map ale w sumie nie do konca
# generalnie propozycje dla partial
# skewed ; biased ; enchanted ;half
# prejudiced ; fragmentary ; fractal
# stronniczy ;
# restricted ; pris? ; distorted ; affected ; applied
# Verb
# inhere (third-person singular simple present inheres,
# present participle inhering, simple past and past participle inhered)
# to be inherent; to be an essential or intrinsic part of;
# to be fixed or permanently incorporated with something 
#
# --- filter
# f = filter # tu jeszcze poszukac synonimow 
#
# --- fan
# a = fan 
# albo a - abanico [es];
# e - eventail [fr](range,array figuratively);
# s - sensu [jp], u - uchiwa [jp]
#
# --- pin 
# v = pin # vortex
# tutaj nazwa "pin" w sumie tak o
# ____________________________ comments end @

shortcuts = dict(\
    p = partial,
    v = pin,
    a = fan,
    m = partial(partial,map),
    f = partial(partial,filter),
    x = argph, )

modules = dict(
    funny = funny,
    filters = filters,
    conds = conds,
    relind = ri,
    dirtyaddons = dirt,
    predefined = pre,)

del partial,pin,fan,argph
del funny,filters

locals().update(shortcuts)
