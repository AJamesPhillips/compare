from six import string_types
from copy import copy


def path_string(path):
  return ' > '.join(path)


messages = []


def print_msg(message):
  messages.append(message)


"""
Will return True if different
"""
def compare(ob1, ob2, path=[]):
  if not (isinstance(ob1, dict) and isinstance(ob1, dict)):
    if ob1 != ob2:
      if (isinstance(ob1, list) and isinstance(ob1, list)):
        # COMPARE as lists
        difference = {'ob1': [], 'ob2': [], 'positions':[]}
        max_length = max(len(ob1), len(ob2))
        for i in range(max_length):
          if i < len(ob2) and i < len(ob1):
            childpath = copy(path)
            childpath.append('i:'+str(i))
            different = compare(ob1[i], ob2[i], childpath)
            if different:
              difference['ob1'].append(ob1[i])
              difference['ob2'].append(ob2[i])
              difference['positions'].append(str(i))
          else:
            if i >= len(ob1):
              difference['ob1'].append('<not present>')
              difference['ob2'].append(ob2[i])
            else:
              difference['ob1'].append(ob1[i])
              difference['ob2'].append('<not present>')
            difference['positions'].append(str(i))
        if difference['ob1']:
          print_msg("{path} lists differed at positions: {positions}\n{ob1}\n{ob2}\n".format(
                      path=path_string(path),
                      positions=','.join(difference['positions']),
                      ob1=difference['ob1'],
                      ob2=difference['ob2']))
          if path != []:
            return difference
        else:
          return False
      else:
        if (isinstance(ob1, set) and isinstance(ob2, set)):
          union = ob1 and ob2
          ob1_extra = ','.join(map(str, list(ob1 - union)))
          ob2_extra = ','.join(map(str, list(ob2 - union)))
          msg = "{path} sets are different".format(path=path_string(path))
          if(ob1_extra):
            msg += " set 1 has extra values:\n{ob1_extra}\n".format(ob1_extra=ob1_extra)
          if(ob2_extra):
            msg += " set 1 is missing values:\n{ob2_extra}\n".format(ob2_extra=ob2_extra)
          print_msg(msg)
        return True
    else:
      return False
  else:
    # COMPARE as dicts
    keys = list(set(ob1.keys()) | set(ob2.keys()))
    for key in keys:
      path_str = path_string(path)
      if key not in ob1 or key not in ob2:
        if key not in ob1:
          i = 2
          val = ob2[key]
        else:
          i = 1
          val = ob1[key]
        print_msg("{} > '{}'  key present in ob{}, absent in ob{}, value={}\n{}\n".format(
                  path_str, key, i, i%2+1, val, path_str))
        continue
      childpath = copy(path)
      childpath.append("'"+key+"'" if isinstance(key, string_types) else str(key))
      different = compare(ob1[key], ob2[key], childpath)
      if different:
        if not isinstance(different, dict):
          pth = path_string(path)
          pth += (" > " if path else "")
          print_msg("{}'{}' value is different:\n{}\n{}\n".format(pth, key, ob1[key], ob2[key]))
  if path == []:
    global messages
    messages.reverse()
    for message in messages:
      print(message)
    messages = []
  return False


if __name__ == '__main__':
  ob1 = {'a':{3:[1,{'c':1,'d':2,'nested_e':['some val']},2],'f':3},'g':3}
  ob2 = {'a':{3:[1,{'c':1,'nested_e':['some val', 'something', 'else']},2,3],'f':3},'g':4}
  print('## Example 1: Comparing two objects: \n{}\n{}\n'.format(ob1, ob2))
  compare(ob1, ob2)

  l1 = [1,3,5,7]
  l2 = [2,4,6,]
  print('\n\n## Example 2: Comparing two simple list: \n{}\n{}\n'.format(l1, l2))
  compare(l1, l2)

  l1 = [1, {'a': 10, 'nested_diff': 2}, {'A', 3}]
  l2 = [1, {'a': 10, 'nested_diff': 3}, {'A', 4}]
  print('\n\n## Example 3: Comparing lists with nested dict and set: \n{}\n{}\n'.format(l1, l2))
  compare(l1, l2)
