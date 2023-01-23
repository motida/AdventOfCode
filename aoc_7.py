class Dir:
  def __init__(self, name, parent=None):
    self.name = name 
    self.parent = parent
    self.files = [] 
    self.dirs = [] # references to other nodes

  def add_child_directory(self, dir):
    # creates parent-child relationship
    print("Adding " + dir.name)
    self.dirs.append(dir) 
    
  def remove_child_directory(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]


curr_dir = None
with open('input7.txt') as f:
    for line in f.readlines():
        line_parts = line.split()
        match line_parts[0]:
            case "$":
                command = line_parts[1]
                match command:
                    case "cd":
                        dir_name = line_parts[2]
                        if dir_name == '..':
                            curr_dir = curr_dir.parent
                        else:
                            dir = Dir(line_parts[2], curr_dir)
                            if dir_name == '/':
                                root_dir = dir
                            else:
                                curr_dir.dirs.append(dir)
                            curr_dir = dir
                    case "ls":
                        curr_sum = 0 
            case "dir":
                pass
            case _:
                curr_dir.files.append(int(line_parts[0]))

small_sizes = []
sizes = []
def dir_size(dir):
    total_size = 0
    total_size += sum(dir.files)
    total_size += sum([dir_size(child_directory) for child_directory in dir.dirs])
    if total_size <= 100000:
        small_sizes.append(total_size)
    sizes.append(total_size)
    return total_size

dir_size(root_dir)
#print(sum(small_sizes))
sizes.sort(reverse=True)

root_size = sizes[0]

unused_space = 70000000 - root_size
print(sorted([x for x in sizes if unused_space + x >= 30000000])[0])






