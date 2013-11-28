Compare
=======

Visualise differences between two objects or lists



## Example

    >>> from compare import compare
    >>> ob1 = {'a': {'b': [1, {'nested_e': ['some val'], 'c': 1, 'd': 2}, 2], 'f': 3}, 'g': 3}
    >>> ob2 = {'a': {'b': [1, {'nested_e': ['some val', 'something'], 'c': 1}, 2, 3], 'f': 3}, 'g': 4}
    >>> compare(ob1, ob2)
    
    'a' > 3 > i:1 > 'nested_e' lists differed at positions: 1
    ['<not present>']
    ['something']
    
    
    'a' > 3 > i:1 > 'd'   in ob1, value=2
    'a' > 3 > i:1
    
    
    'a' > 3 lists differed at positions: 3
    ['<not present>']
    [3]
    
    
    'g' was different:
    3
    4
    
