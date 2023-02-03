import sys 

def read_input():
    with open('input12.txt') as f:
        mat = [list(line.strip()) for line in f.readlines()]
    return mat
    

def convert_mat_to_ints(mat):    
    a_starts = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'S':
                start = (i, j)
                a_starts.append((i, j))
                mat[i][j] = ord('a') - 97
            elif mat[i][j] == 'E':
                end = (i, j)
                mat[i][j] = ord('z') - 97
            elif mat[i][j] == 'a':
                a_starts.append((i, j))
                mat[i][j] = ord(mat[i][j]) - 97
            else:
                mat[i][j] = ord(mat[i][j]) - 97
    return mat, start, end, a_starts

def generate_adj_list(mat, start_vertex, end_vertex):
    adj_list = {}
    vertices = {start_vertex, end_vertex}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            adj_list[(i, j)] = []
            # up 
            if i-1 >= 0 and mat[i-1][j] - 1 <= mat[i][j]:
                adj_list[(i,j)].append((i-1,j))  
                vertices.add((i-1,j))  
            # down
            if i+1 < len(mat) and mat[i+1][j] - 1 <= mat[i][j]:
                adj_list[(i,j)].append((i+1,j)) 
                vertices.add((i+1,j))
            # left
            if j-1 >= 0 and mat[i][j-1] - 1 <= mat[i][j]:
                adj_list[(i,j)].append((i,j-1))
                vertices.add((i,j-1))
            # right
            if j+1 < len(mat[i]) and mat[i][j+1] - 1 <= mat[i][j]:
                adj_list[(i,j)].append((i,j+1)) 
                vertices.add((i,j+1))

    return adj_list, list(vertices)


def shortest_path(adj_list, start_vertex, vertices):
    unvisited_vertices = set(vertices[:])
    visited_vertices = set()
    distances = {vertex: sys.maxsize for vertex in vertices}
    distances[start_vertex] = 0

    while unvisited_vertices:
        unvisited_distances = {k: distances[k] for k in distances if k in unvisited_vertices}
        curr_vertex = min(unvisited_distances, key=unvisited_distances.get)
        for vertex in adj_list[curr_vertex]:
            if vertex in unvisited_vertices:
                distances[vertex] = min(distances[curr_vertex] + 1, distances[vertex])
        visited_vertices.add(curr_vertex)
        unvisited_vertices.remove(curr_vertex)

    return distances
        


mat = read_input()
mat, start_vertex, end_vertex, a_start_vertices = convert_mat_to_ints(mat)

adj_list, vertices = generate_adj_list(mat, start_vertex, end_vertex)

# part I
distances = shortest_path(adj_list, start_vertex, vertices)

print(distances[end_vertex])


# part II
flipped_end_vertex, filipped_start_vertex = start_vertex, end_vertex 
flipped_adj_list = {v: [] for v in vertices}
for from_vertex in adj_list:
    for to_vertex in adj_list[from_vertex]:
        flipped_adj_list[to_vertex].append(from_vertex)

flipped_distances = shortest_path(flipped_adj_list, filipped_start_vertex, vertices)

a_start_distances = {k: flipped_distances[k] for k in a_start_vertices}

sorted_a_start_distnances = sorted(a_start_distances.items(), key=lambda x:x[1])
print(sorted_a_start_distnances[0][1])

