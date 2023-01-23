with open('input8.txt') as f:
    mat = [[int(n) for n in line.strip()] for line in f.readlines()]

def calc_visibility(line):
    visability = [0 for _ in line]
    visability[0] = 1
    max_value = line[0]
    for i in range(1, len(line)-1):
        if line[i] > max_value:
            max_value = line[i]
            visability[i] = 1
        else:
            visability[i] = 0
    return visability


def find_max_value(vec, val):
    ret_val = 0
    for i in range(len(vec)-1,-1,-1):
        ret_val +=1
        if vec[i] >= val:
            return ret_val
            
    return ret_val        


def calc_visibility_from_tree(line):
    visability = [0 for _ in line]
    visability[0] = 0#
 
    for i in range(1, len(line)):
        visability[i] = find_max_value(line[0:i], line[i])
       
    return visability


def print_mat(mat):
    for line in mat:
        print(line)

def transpose_mat(mat):
    transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return transposed

def add_mat(mat1, mat2):
    added = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return added

def mult_mat(mat1, mat2):
    added = [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return added

def sum_visabilty(mat):
    total_visable = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                total_visable += 1
    return total_visable

def max_visabilty(mat):
    max_val = max([max(line) for line in mat])
    return max_val

#print(transpose_mat(mat))

# horz_left_right = [calc_visibility(line) for line in mat]
# horz_right_left = [calc_visibility(line[::-1])[::-1] for line in mat]
# vert_left_right = transpose_mat([calc_visibility(line) for line in transpose_mat(mat)])
# vert_right_left = transpose_mat([calc_visibility(line[::-1])[::-1] for line in transpose_mat(mat)])

# print_mat(horz_left_right)
# print()
# print_mat(horz_right_left)
# print()
# print_mat(vert_left_right)
# print()
# print_mat(vert_right_left)
# print()
# summed_mat = add_mat(add_mat(add_mat(horz_left_right, horz_right_left), vert_left_right), vert_right_left)
# print_mat(summed_mat)
# print()
# print(sum_visabilty(summed_mat))



#part 2


horz_left_right = [calc_visibility_from_tree(line) for line in mat]
horz_right_left = [calc_visibility_from_tree(line[::-1])[::-1] for line in mat]
vert_left_right = transpose_mat([calc_visibility_from_tree(line) for line in transpose_mat(mat)])
vert_right_left = transpose_mat([calc_visibility_from_tree(line[::-1])[::-1] for line in transpose_mat(mat)])




print()
print_mat(mat)
print()
print_mat(horz_left_right)
print()
print_mat(horz_right_left)
print()
print_mat(vert_left_right)
print()
print_mat(vert_right_left)
print()
mult_mat = mult_mat(mult_mat(mult_mat(horz_left_right, horz_right_left), vert_left_right), vert_right_left)
#print_mat(mult_mat)
print()
print(max_visabilty(mult_mat))




        

