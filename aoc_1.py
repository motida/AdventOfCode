with open('input.txt') as f:
    max_sum = 0
    curr_sum = 0
    for line in f.readlines():
        if line.rstrip():
            curr_sum += int(line)
        else:
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
max_sum = max(curr_sum, max_sum)     
print(max_sum)       