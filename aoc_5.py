from itertools import islice

with open('input5.txt') as f:

    lines = []
    instructs = []
    past_conf = False
    for line in f.readlines():
        if len(line) == 1:
            past_conf = True
        elif not past_conf:
            lines.append(line[:-1])
        else:
            instructs.append(line[:-1])
    axis = lines.pop()
    num_of_stacks = (int(axis.split()[-1]))
    stacks = [[] for _ in range(num_of_stacks)]
    while lines:
        line = lines.pop()
        for i, c in enumerate([line[i] for i in range(1, len(line), 4) ]):
            if c.strip():
                stacks[i].append(c)
    # pt1
    # for instruct in instructs:
    #     _, move, _, from_stack, _, to_stack = instruct.split(' ') 
    #     for _ in range(int(move)):
    #         stacks[int(to_stack)-1].append(stacks[int(from_stack)-1].pop())
    # result = ''.join([stack[-1] for stack in stacks])
    # pt2
    for instruct in instructs:
       _, move, _, from_stack, _, to_stack = instruct.split(' ') 
       pile = []
       for _ in range(int(move)):
            pile.append(stacks[int(from_stack)-1].pop())
       pile.reverse() 
       for c in pile:
           stacks[int(to_stack)-1].append(c) 
    result = ''.join([stack[-1] for stack in stacks])

    print(result)
