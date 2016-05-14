from six import string_types


def path_string(path):
  return ' > '.join(path)


messages = []


def print_msg(message):
  messages.append(message)


def _comp(ob1, ob2, path):
  if ob1 == ob2:
    return False
  else:
    if (isinstance(ob1, dict) and isinstance(ob1, dict)):
      # COMPARE as dicts
      _comp_dicts(ob1, ob2, path)
      return {'different': True}
    elif (isinstance(ob1, list) and isinstance(ob1, list)):
      # COMPARE as lists
      _comp_lists(ob1, ob2, path)
      return ['different']
    elif (isinstance(ob1, set) and isinstance(ob2, set)):
      # COMPARE as sets
      _comp_sets(ob1, ob2, path)
      return {'different'}
    return True


def _comp_dicts(ob1, ob2, path):
  keys = sorted(list(set(ob1.keys()).union(set(ob2.keys()))), key=lambda a: str(a))
  for key in keys:
    key_str = "'"+key+"'" if isinstance(key, string_types) else str(key)
    path.append(key_str)
    pth = path_string(path)
    if key in ob1 and key in ob2:
      different = _comp(ob1[key], ob2[key], path)
      if different and isinstance(different, bool):
        print_msg("{} dict value is different:\n{}\n{}\n".format(pth, ob1[key], ob2[key]))
    else:
      if key not in ob1:
        i = 2
        val = ob2[key]
      else:
        i = 1
        val = ob1[key]
      print_msg("{} dict key present in ob{}, absent in ob{}, value={}\n".format(
                pth, i, i%2+1, val))
    path.pop()


def _comp_lists(ob1, ob2, path):
  difference_ob1 = []
  difference_ob2 = []
  difference_positions = []

  max_length = max(len(ob1), len(ob2))
  for i in range(max_length):
    if i < len(ob1) and i < len(ob2):
      path.append('i:'+str(i))
      different = _comp(ob1[i], ob2[i], path)
      path.pop()
      if different and isinstance(different, bool):
        difference_ob1.append(ob1[i])
        difference_ob2.append(ob2[i])
        difference_positions.append(str(i))
    else:
      if i >= len(ob1):
        difference_ob1.append('<not present>')
        difference_ob2.append(ob2[i])
      else:
        difference_ob1.append(ob1[i])
        difference_ob2.append('<not present>')
      difference_positions.append(str(i))
  if difference_ob1:
    print_msg("{path} lists differed at positions: {positions}\n{ob1}\n{ob2}\n".format(
                path=path_string(path),
                positions=','.join(difference_positions),
                ob1=difference_ob1,
                ob2=difference_ob2))
  else:
    return False

def _comp_sets(ob1, ob2, path):
  union = ob1.union(ob2)
  ob1_extra = ','.join(map(str, sorted(list(union - ob1))))
  ob2_extra = ','.join(map(str, sorted(list(union - ob2))))
  msg = "{path} sets are different:\n".format(path=path_string(path))
  if(ob1_extra):
    msg += "Set 1 has extra values:\n{ob1_extra}\n".format(ob1_extra=ob1_extra)
  if(ob2_extra):
    msg += "Set 1 is missing values:\n{ob2_extra}\n".format(ob2_extra=ob2_extra)
  print_msg(msg)


"""
Will return True if different
"""
def compare(ob1, ob2, return_messages=False):
  different = _comp(ob1, ob2, ['.'])
  global messages
  for message in messages:
    print(message)

  msgs = messages
  messages = []
  return msgs if return_messages else different


if __name__ == '__main__':
  ob1 = {'g':3, 'a':{'f':3, 3:[1,{'c':1,'d':2,'nested_e':['some val'                     ]},2  ]}}
  ob2 = {'g':4, 'a':{'f':3, 3:[1,{'c':1,      'nested_e':['some val', 'something', 'else']},2,3]}}
  print('## Example 1: Comparing two objects: \n{}\n{}\n\n'.format(ob1, ob2))
  result = compare(ob1, ob2, True)
  expected = [
    ". > 'a' > 3 > i:1 > 'd' dict key present in ob1, absent in ob2, value=2\n",
    ". > 'a' > 3 > i:1 > 'nested_e' lists differed at positions: 1,2\n['<not present>', '<not present>']\n['something', 'else']\n",
    ". > 'a' > 3 lists differed at positions: 3\n['<not present>']\n[3]\n", ". > 'g' dict value is different:\n3\n4\n"
  ]
  assert not compare(result, expected)


  l1 = [1,3,5,7]
  l2 = [2,4,6,]
  print('## Example 2: Comparing two simple list: \n{}\n{}\n'.format(l1, l2))
  result = compare(l1, l2, True)
  expected = [". lists differed at positions: 0,1,2,3\n[1, 3, 5, 7]\n[2, 4, 6, '<not present>']\n"]
  assert not compare(result, expected)


  l1 = [1, {'a': 10, 'nested_diff': 2}, {'A', 3}]
  l2 = [1, {'a': 10, 'nested_diff': 3}, {'A', 4}]
  print('## Example 3: Comparing lists with nested dict and set: \n{}\n{}\n'.format(l1, l2))
  result = compare(l1, l2, True)
  expected = [
    ". > i:1 > 'nested_diff' dict value is different:\n2\n3\n",
    '. > i:2 sets are different:\nSet 1 has extra values:\n4\nSet 1 is missing values:\n3\n',
  ]
  assert not compare(result, expected)

