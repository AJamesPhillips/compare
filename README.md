Compare
=======

Visualise differences between two dicts or lists



## Example

    >>> from compare import compare
    >>> ob1 = {'a': {'b': [1, {'nested_e': ['some val'], 'c': 1, 'd': 2}, 2], 'f': 3}, 'g': 3}
    >>> ob2 = {'a': {'b': [1, {'nested_e': ['some val', 'something'], 'c': 1}, 2, 3], 'f': 3}, 'g': 4}
    >>> compare(ob1, ob2)


    'g' value is different:
    3
    4

    'a' > 'b' lists differed at positions: 3
    ['<not present>']
    [3]

    'a' > 'b' > i:1 > 'd'  key present in ob1, absent in ob2, value=2
    'a' > 'b' > i:1

    'a' > 'b' > i:1 > 'nested_e' lists differed at positions: 1
    ['<not present>']
    ['something']

