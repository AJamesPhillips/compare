Compare
=======

Visualise differences between two dicts or lists



## Example

    >>> from compare import compare
    >>> ob1 = {'a': 3, 'b': {'c': [0, {'d': 1, 'e': 2, 'nested_f': ['some val']             }, 2   ], 'g': {3, 4}}}
    >>> ob2 = {'a': 4, 'b': {'c': [0, {'d': 1,         'nested_f': ['some val', 'something']}, 2, 3], 'g': {3, 5}}}
    >>> compare(ob1, ob2)

    . > 'a' dict value is different:
    3
    4

    . > 'b' > 'c' > i:1 > 'e' dict key present in ob1, absent in ob2, value=2

    . > 'b' > 'c' > i:1 > 'nested_f' lists differed at positions: 1
    ['<not present>']
    ['something']

    . > 'b' > 'c' lists differed at positions: 3
    ['<not present>']
    [3]

    . > 'b' > 'g' sets are different:
    Set in ob1 has extra values:
    5
    Set in ob1 is missing values:
    4
