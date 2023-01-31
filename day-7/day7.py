def update_file_size(fname):
    pass
data = open("test_input", "r")
terminal_output = data.readlines()
curr_dir = ""
curr_dir_size = 0
dir_size_dict = {}
dir_strings =[]
dir_sizes = []
dir_contains={}
for line in terminal_output:
    word_array = line.split()
    if word_array[0] == "$":
        if  word_array[1] == "cd" and not(word_array[2] == ".."):
            if not dir_strings =='':
                dir_contains.update({curr_dir: dir_strings})
            dir_sizes.append(curr_dir_size)
            dir_size_dict.update({curr_dir:curr_dir_size})
            curr_dir = word_array[2]
            curr_dir_size = 0
            dir_strings = []
    else:
        if word_array[0].isnumeric():
            curr_dir_size += int(word_array[0])
        elif word_array[0] == "dir":
            dir_strings.append(word_array[1])

dir_size_dict.update({curr_dir: curr_dir_size})
test =[*dir_contains]
test = test[::-1]
for key in test:
    contains = dir_contains[key]
    new_size = 0
    for x in contains:
        new_size += dir_size_dict[x]
    new_size += dir_size_dict[key]
    dir_size_dict.update({key: new_size})
memory = sum(x for x in dir_size_dict.values() if x <= 100000)
print(memory)
print(dir_size_dict )
        
