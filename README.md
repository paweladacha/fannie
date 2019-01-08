# fannie

Simple yet very usefull implementation of partial function.

## Contents
- [Intendet use](#intended-use)
- [How it works?](#how-it-works)
- [Extension](#extension)
- [Usage examples](#usage-examples)
    - [basic use of partial object](#basic-use-of-partial-object)
    - [fan and pin usage](#fan-and-pin-usage)

## Intended use
Day-to-day use and rapid protyping via interpreter, ipython or Jupyter notebook.

## How it works?
Simple differences between this and *functools* implementation are mutable attributes `.f` (stores function) and `.a` (stores arguments/signature).

More important difference lays in usage. The "variable placeholder" (`argph`) can be used to intuivelly and explicitlly point variable argument. In other words user can literally point with his finger wich argument should be variable.

Of course *keywords argument* solve this inconvenience but some built-in functions and methods (python 3.5) does not provide this feature. 
Also, when it comes to quick prototyping signatures sticked with 'key=value' parameters become are "too explicit".

## Extension
Two functions defined in tools help in creation of more complex partials or "flows": *fan* and *pin*.
They can be seen as two basic ways of connecting compenents in electric circuits:
- fan - parallel, calls all given functions with the same variable argument.
- pin - sequential, uses the output of the previous call as an input to subsequent call.

## Usage examples

### basic use of partial object

```python

import fannie

partial = fannie.p
sample = [1, 2, 3]
func = lambda x:x*2


map_mul_by_2 = partial(map, func)
map_sample = partial(map, argph, sample)

list(map_mul_by_2(sample))        # [2,4,6]
list(map_mul_by_2([3, 2, 1]))     # [6,4,2]
list(map_sample(func))            # [2,4,6]
list(map_sample(lambda x: x*3))   # [3,6,9]


# some magic:
# partial(partial,func) -> partial that returns func partial

map_ = partial(partial, map)
map_mul_by_2_v2 = map_(func)
list(map_mul_by_2_v2(sample))     # [2,4,6]
                                  # or equivalently
list(map_(func)(sample))          # [2,4,6]

# or without all those "list" calls obscuring this example
# and with use of predefined solution

fannie.m(func)(sample)            # [2,4,6]
```

### fan and pin usage

```python
import fannie as fx

sample = ''' - [primes](https://github.com/paweladacha/primes)
- [fannie](https://github.com/paweladacha/fannie)'''

# fx.a = fan # for array
# fx.v = pin # for vertical

get_fields = fx.p(fx.a,[
    lambda ar:ar[0].partition('[')[-1],
    lambda ar:ar[1].partition(')')[0], ]) # -> generator

get_item_dict = fx.p(fx.v,[
    get_fields,
    lambda i:dict(zip(('title','url'),i)) ]) # -> dict

parse_single_item = fx.p(fx.v,[
    fx.p(str.split,fx.x,']('),
    get_item_dict ]) # -> dict

parse_input = fx.p(fx.v,[str.splitlines,
    fx.p(map,parse_single_item),list]) # -> list

parse_input(sample) # ->
# [{'title': 'primes', 'url': 'https://github.com/paweladacha/primes'},
#  {'title': 'fannie', 'url': 'https://github.com/paweladacha/fannie'}]
```

