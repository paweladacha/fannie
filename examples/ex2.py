import fannie as fx

sample = ''' - [primes](https://github.com/paweladacha/primes)
- [fannie](https://github.com/paweladacha/fannie)'''

# fx.a = fan # for array
# fx.v = pin # for vertical

get_fields = fx.p(fx.a, [
    lambda ar:ar[0].partition('[')[-1],
    lambda ar:ar[1].partition(')')[0], ])  # -> generator

get_item_dict = fx.p(fx.v, [
    get_fields,
    lambda i:dict(zip(('title', 'url'), i))])  # -> dict

parse_single_item = fx.p(fx.v, [
    fx.p(str.split, fx.x, ']('),
    get_item_dict])  # -> dict

parse_input = fx.p(fx.v, [str.splitlines,
                          fx.p(map, parse_single_item), list])  # -> list

parse_input(sample)
# ->
# [{'title': 'primes', 'url': 'https://github.com/paweladacha/primes'},
#  {'title': 'fannie', 'url': 'https://github.com/paweladacha/fannie'}]
