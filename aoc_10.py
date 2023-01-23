with open('input10.txt') as f:
    instructions = [line.strip().split() for line in f.readlines()]

X = 1

CYCLES=[20, 60, 100, 140, 180, 220]

cycles_values = [X]

for instruction in instructions:
    op = instruction[0]
    match op:
        case 'noop':
            cycles_values.append(X)  
        case 'addx':
            cycles_values += [X,X]
            X += int(instruction[1])

print(sum([cycles_values[i] * i for i in CYCLES]))

for c in range(0, len(cycles_values)-1, 40):
    x = ["#" if i-1-c in (cycles_values[i]-1, cycles_values[i], cycles_values[i]+1) else "." for i in range(c+1, c+41)]
    print("".join(x))

