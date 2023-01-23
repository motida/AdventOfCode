# with open('input3.txt') as f:
#     sum = 0

#     for line in f.readlines():
       
#         dup = tuple(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0]
#         sum += ord(dup) - 38 if dup.isupper() else ord(dup) - 96
#     print(sum)

with open('input3.txt') as f:
    sum = 0
    while True:
        line1= f.readline().strip()
        if not line1:
            break
        line2, line3 = f.readline().strip(), f.readline().strip()
        dup = tuple(set(line1).intersection(set(line2)).intersection(set(line3)))[0]
        sum += ord(dup) - 38 if dup.isupper() else ord(dup) - 96
    print(sum)
