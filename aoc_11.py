import sys
sys.set_int_max_str_digits(0)
from functools import reduce

class Monkey():
    def __init__(self, items, op, divisor, true_throw, false_throw):
        self.items = items
        self.op = op 
        self.divisor = divisor
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspections = 0


def read_input():
    monkies = []
    fp = open('input11.txt')
    while 1:
        monkey_line = fp.readline()
        if not monkey_line:
            break
        monkey = int(monkey_line[:-2].split()[1])

        #print(monkey)
        items_line = fp.readline()
        items = [int(x) for x in (items_line[18:].strip().split(", "))]
        #print(items)
        op_line = fp.readline()
        op = op_line[13:].strip()
        #print(op)
        divisible_line = fp.readline()
        divisible = int(divisible_line[21:].strip())
        #print(divisible)
        true_line = fp.readline()
        true_throw = int(true_line[29:].strip())
        false_line = fp.readline()
        false_throw = int(false_line[30:].strip())
        #print(true_throw, false_throw)
        fp.readline()
        monkies.append(Monkey(items, op, divisible, true_throw, false_throw))
        
    return monkies


monkies = read_input()
modulo = reduce(lambda a, b: a * b, [monkey.divisor for monkey in monkies])
print ([monkey.divisor for monkey in monkies])
print(modulo)
print(list([monkey.items for monkey in monkies]))
round = 0
while any([monkey.items for monkey in monkies]) and round < 10000:  # < 20
    round += 1
    for monkey in monkies:
        for item in monkey.items:
            #print(item)
            val = (eval((monkey.op.replace('old', str(item)))[6:]))
            val %= modulo 
            #val_str = (monkey.op.replace('old', str(item)))[6:]
            #compiled = compile(val_str, '<str>', 'eval')
            #val = eval(compiled)
            #num1, op, num2 = (monkey.op[6:]).split()
            # if num2 != 'old':
            #     num2_i = int(num2)
            #print (num1, op, num2, val)
            #val = (int(num1) + int(num2)) 
            # if op == '+' and num2 == 'old':
            #     if np.mod((2 * (np.mod(item, monkey.divisible))), monkey.divisible) == 0:
            #         monkies[monkey.true_throw].items.append(2 * item)
            #     else:
            #         monkies[monkey.false_throw].items.append(2 * item)
            # if op == '+' and num2 != 'old':   
            #     if np.mod(((np.mod(num2_i,  monkey.divisible)) + (np.mod(item, monkey.divisible))), monkey.divisible) == 0:
            #         monkies[monkey.true_throw].items.append(num2_i + item)
            #     else:
            #         monkies[monkey.false_throw].items.append(num2_i + item)                 

            # if op == '*' and num2 == 'old':
            #     if np.mod(((np.mod(item, monkey.divisible)) ** 2), monkey.divisible) == 0:
            #         monkies[monkey.true_throw].items.append(item ** 2)
            #     else:
            #         monkies[monkey.false_throw].items.append(item ** 2)
            # if op == '*' and num2 != 'old':   
            #     if np.mod(((np.mod(num2_i, monkey.divisible)) * (np.mod(item, monkey.divisible))), monkey.divisible) == 0:
            #         monkies[monkey.true_throw].items.append(num2_i * item)
            #     else:
            #         monkies[monkey.false_throw].items.append(num2_i * item)                 

            if val % monkey.divisor == 0:
                monkies[monkey.true_throw].items.append(val)
            else:
                monkies[monkey.false_throw].items.append(val)
        monkey.inspections += len(monkey.items)
        monkey.items = []
    print("round", round)
    #print(list([monkey.items for monkey in monkies]))
    #print()
two_most_inspected = sorted([monkey.inspections for monkey in monkies], reverse=True)[0:2]
print(two_most_inspected)
print(two_most_inspected[0] * two_most_inspected[1])

