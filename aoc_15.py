import re

Y = 2_000_000
START_SCAN = 0
END_SCAN = 4_000_000


def read_input():
    sensors = []
    beacons = []
    with open('input15.txt') as f:
        for line in f.readlines():
            (sx, sy, bx, by) = re.findall(r'[-]*\d+', line)
            sensors.append((int(sx), int(sy)))
            beacons.append((int(bx), int(by)))

    return sensors, beacons

def man_distance(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1]- p2[1])

def man_distances(sensors, beacons):
    return [man_distance(p1, p2) for p1, p2 in zip(sensors, beacons)]

def find_free_xs_in_line(sensors, beacons, man_dists, Y=Y):
    no_beacons = set()

    sensors_x_set = set([x for (x, y) in sensors if y==Y])
    beacons_x_set = set([x for (x, y) in beacons if y==Y])
    for i, sensor in enumerate(sensors):
        if sensor[1] - man_dists[i] <= Y <= sensor[1] + man_dists[i]:
            y_dist = abs(Y-sensor[1])
            x_dist = man_dists[i] - y_dist
            xs = set(range(sensor[0] - x_dist, sensor[0] + x_dist + 1))
            no_beacons = no_beacons.union(xs) 


    no_beacons = no_beacons.difference(beacons_x_set)
    no_beacons = no_beacons.difference(sensors_x_set)

    return no_beacons




def print_map(sensors, beacons, man_dists):

    min_x = min(0, min([pos[0] for pos in sensors + beacons]))
    min_y = min(0, min([pos[1] for pos in sensors + beacons]))
    max_x = max(20, max([pos[0] for pos in sensors + beacons]))
    max_y = max(20, max([pos[1] for pos in sensors + beacons]))

    map = {(y, x): '.' for x in range(min_x, max_x +1) for y in range(min_y, max_y + 1)}

    for y in range(min_y, max_y + 1):
        for x in find_free_xs_in_line(sensors, beacons, man_dists, Y=y):
            map[(y, x)] = '$'
    for sensor in sensors:
        map[(sensor[1], sensor[0])] = 'S'
    for beacon in beacons:
        map[(beacon[1], beacon[0])] = 'B'

    print((min_x, max_x), (min_y, max_y))
    for y in range(0, 20 + 1):
        print()
        for x in range(0, 20 + 1):
            print(map[(y, x)], end='')
    
    print()





def scan_line(sensors, beacons, man_dists, Y, end_scan):
    no_beacons = set()
    xs_ranges = []
    for i, sensor in enumerate(sensors):
        if sensor[1] - man_dists[i] <= Y <= sensor[1] + man_dists[i]:
            y_dist = abs(Y-sensor[1])
            x_dist = man_dists[i] - y_dist
            xs_ranges.append((sensor[0] - x_dist, 'S'))
            xs_ranges.append((sensor[0] + x_dist, 'E'))

    xs_ranges = sorted(xs_ranges, key=lambda x: x[0])
  
    level = 0
    for i, xs_range in enumerate(xs_ranges):
        if xs_range[1] == 'S':
            level += 1
        if xs_range[1] == 'E':
            level -= 1
        if level == 0 and xs_range[0] > 0 and xs_range[0] <= end_scan and i < len(xs_ranges) - 1 \
            and xs_ranges[i+1][0] != xs_range[0] and xs_ranges[i+1][0] != xs_range[0] + 1 and Y <=end_scan:
            return xs_range[0] + 1

    return None


def find_distress_beacon(sensors, beacons, man_dists, scan_start, scan_end):
    for y in range(scan_start, scan_end + 1):
        x = scan_line(sensors, beacons, man_dists, y, scan_end) 
        if x and (x, y) not in sensors and (x, y) not in beacons:
            return((x, y))
    


sensors, beacons = read_input()

man_dists = man_distances(sensors, beacons)

xs = find_free_xs_in_line(sensors, beacons, man_dists, Y)
print('part1' , len(xs))
x, y = find_distress_beacon(sensors, beacons, man_dists, START_SCAN , END_SCAN)
print('part2', x * 4_000_000 + y)

