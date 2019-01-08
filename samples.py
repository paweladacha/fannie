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
