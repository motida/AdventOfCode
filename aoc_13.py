def read_input():
    with open('input13.txt') as f:
        pairs = []
        while 1:
            p1 = f.readline().strip()
            if not p1:
                break
            p2 = f.readline().strip()
            pair = (eval(p1), eval(p2))
            f.readline()  # skip empty line
            pairs.append(pair)

    return pairs

def check_pair(pair):
    (l, r) = pair
    if type(l) == int and type(r) == int:
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None
    if type(l) == int and type(r) == list:
         return check_pair(([l], r))
    if type(r) == int and type(l) is list:
         return check_pair((l, [r]))  
    # type(l) == list and type(r) == list
    z = zip(l, r)
    for l1, r1 in z:
        res = check_pair((l1, r1)) 
        if res is None:
            continue
        else:
            return res
    if len(l) < len(r):
        return True
    elif len(l) > len(r):
        return False
    else:
        return None

pairs = read_input()


proper_pairs = []

#print(pairs)
#print(check_pair(pairs[1]))
for i, pair in enumerate(pairs):
    if check_pair(pair):
        proper_pairs.append(i+1) # indexing start at 1

#print(len(pairs))
#print(proper_pairs)
print(sum(proper_pairs))


signals = [item for pair in pairs for item in pair]
signals.append([[2]])
signals.append([[6]])

from functools import cmp_to_key

def comparator(l, r):
    res = check_pair((l, r))
    if res:
        return -1
    else:
        return 1


sorted_signals = sorted(signals, key=cmp_to_key(comparator))

print((sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))




    