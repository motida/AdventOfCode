POUR_POINT = (0, 500)

def read_input():
    paths = []
    with open('input14.txt') as f:
        for line in f.readlines():
            paths.append([eval(p) for p in line.strip().split(' -> ')])
    return paths
 
def create_field(paths, puzzle_part=1):
    points = [point for path in paths for point in path]
    max_x = max(point[0] for point in points) + (100 if puzzle_part == 1 else 1000)
    max_y = max(point[1] for point in points) + (0 if puzzle_part == 1 else 2)

    field = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for path in paths:
        for i in range(0, len(path) -1):
            from_point, to_point = path[i], path[i+1]
            if from_point[0] != to_point[0]:
                y = from_point[1]
                if from_point[0] <= to_point[0]:
                    for x in range(from_point[0], to_point[0] + 1):
                        field[y][x] = '#'
                else:
                    for x in range(from_point[0], to_point[0] - 1, -1):
                        field[y][x] = '#'
            else:   #  if from_point[1] != to_point[1]:
                x = from_point[0]
                if from_point[1] <= to_point[1]:
                    for y in range(from_point[1], to_point[1] + 1):
                        field[y][x] = '#'
                else:
                    for y in range(from_point[1], to_point[1] - 1, -1):
                        field[y][x] = '#'

    return field


def print_field(field, cycle):
    """
    Helper function for debug
    """
    print()
    print('CYCLE', cycle)
    for y in range(12):
        for x in range(450, 550):
            print(field[y][x], end="") 
        print()   


def simulate(field, puzzle_part=1):
    cycle = 0
    units = 0
    sand_falling =  False
    while True:
        cycle += 1
        if not sand_falling:
            y, x = POUR_POINT
            if field[y][x] == 'o':
                break
            field[y][x] = '+'
            sand_falling = True
        else: # sand_falling
            if y == len(field) - 1 and puzzle_part == 1:
                break
            if y == len(field) - 2 and puzzle_part == 2:
                field[y][x] = 'o'
                units += 1
                sand_falling = False
                continue
            if field[y + 1][x] == '.':
                field[y][x] = '.'
                y += 1
                field[y][x] = '+'
            elif field[y + 1][x - 1] == '.':
                field[y][x] = '.'
                y += 1
                x -= 1
                field[y][x] = '+'
            elif field[y + 1][x + 1] == '.':
                field[y][x] = '.'
                y += 1
                x += 1
                field[y][x] = '+'
            else:
                field[y][x] = 'o'
                units += 1
                sand_falling = False
                      
    return units


paths = read_input()

# part1
field = create_field(paths, 1)
units = simulate(field, 1)
print('units', units)

# part 2
field = create_field(paths, 2)
units = simulate(field, 2)
print('units', units)

