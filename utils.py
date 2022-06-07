from math import sqrt
from random import sample

_zip = zip


def map_and_filter(s, map_fn, filter_fn):
	>>> square = lambda x: x * x
    >>> is_odd = lambda x: x % 2 == 1
    >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)



    return [map_fn(x) for x in s if filter_fn(x)]



def key_of_min_value(d):
	>>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)


    >>> key_of_min_value(letters)
    return min(d, key=lambda x: d[x])



def zip(*sequences):
	>>> zip(range(0, 3), range(3, 6))
	>>> for a, b in zip([1, 2, 3], [4, 5, 6]):
    ...     print(a, b)



    >>> for triple in zip(['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi']):
    ...     print(triple)



    return list(map(list, _zip(*sequences)))



def enumerate(s, start=0):
	>>> enumerate([6, 1, 'a'])
	>>> enumerate('five', 5)

	return list(zip(range(start, start + len(s)), s))



def distance(pos1, pos2):
	>>> distance([1, 2], [4, 6])
	return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def mean(s):
	>>> mean([-1, 3])
	>>> mean([0, -3, 2, -1])

	assert len(s) > 0, 'empty list'
    return sum(s) / len(s)





