with open('input9.txt') as f:
    instructions = [line.strip().split() for line in f.readlines()]

KNOTS = 10   # 0 = Head, min knots 2 (for part 1 - head + tail knot), 10 for part 2 (head + 9 knots)

(sx, sy) = (0, 0)  # Start position
tx = [0 for _ in range(KNOTS)]  # Knots x pos
ty = [0 for _ in range(KNOTS)]  # Knots y pos


visited = set()  # set of visited pos by tail 
visited.add((0 ,0))


def print_mat():
    '''
    Helper method for printing all visited positions 
    '''

    min_x, min_y, max_x, max_y = -150, -150, 100, 100
    for y in range(max_y, min_y-1, -1):
        for x in range(min_x, max_x+2):
            try:
                t = list(zip(tx,ty)).index((x,y))
            except:
                t = -1
            if t == 0:
                print('H', end='')
            elif t != -1:
                print(t, end='') 
            elif (x, y) == (sx, sy):
                print('s', end='') 
            elif (x, y) in visited:
                print('$', end='')
            else:
                print('.', end='')
        print()
    print()

#print_mat()


def calc_knot(hx, hy, tx, ty):
    
    # covered
    if (hx, hy) == (tx, ty):
        return  tx, ty
    # 1 adjacent
    if (abs(hx-tx) == 1 and ty == hy) or (abs(hy-ty) == 1 and tx == hx):
        return  tx, ty
    # diagonal simple
    if (abs(hx-tx) == 1 and abs(hy-ty) == 1):
        return  tx, ty
     
    if hx-tx == 2 or hx-tx == 1:
        tx +=1
    elif hx-tx == -2 or hx-tx == -1:
        tx -=1
    else:
        pass
    
    if hy-ty == 2 or hy-ty == 1:
        ty += 1
    elif hy-ty == -2 or hy-ty == -1:
        ty -= 1
    else:
        pass

    return tx, ty

for instruction in instructions:
    (direction, steps) = instruction
    print(direction, steps)
    for step in range(int(steps)):
        match direction:
            case 'R':
                tx[0] += 1
            case 'L':
                tx[0] -= 1
            case 'U':
                ty[0] += 1
            case 'D':
                ty[0] -= 1
        #visited.add((tx[0],ty[0]))

        #print('step ', step + 1)
        #print_mat()
        for i in range(1, KNOTS):
            (tx[i], ty[i]) = calc_knot(tx[i-1], ty[i-1], tx[i], ty[i])
            #print('knot', i)
        #print_mat()
        visited.add((tx[KNOTS-1],ty[KNOTS-1]))
        
        

print_mat()

print(len(visited))



