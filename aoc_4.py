with open('input4.txt') as f:
    sum_contains = 0
    sum_overlap = 0
    for line in f.readlines():
        [[l1, l2], [l3, l4]]= ([map(int, rn.split('-')) for rn in line.strip().split(',')])
        s1 = set(range(l1, l2+1))
        s2 = set(range(l3, l4+1))
        if s1.issubset(s2) or s1.issuperset(s2):
            sum_contains += 1 
        if s1.intersection(s2):
            sum_overlap += 1   
        #if (l1 <= l3 and l2 >= l4) or (l1 >=  l3 and l2 <= l4):
        #    sum_overlap += 1
print(sum_overlap)
