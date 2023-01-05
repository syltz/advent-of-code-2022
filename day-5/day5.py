import re
data = open("input", "r")
line = data.readline()
line_number = -1
column_numbers = []
init_lines = []
# Find out a) how many columns of boxes there are
# b) where the numbering of the box stacks is
# c) where the movement instructions begin
while line.strip():
    init_lines.append(line)
    line_number += 1
    char_number = -1
    for char in line:
        char_number += 1
        if char.isdigit():
            column_numbers.append(char_number)
    line = data.readline()
stacks = [""]* len(column_numbers)
# Create initial stacks of boxes
for i in range(0, len(init_lines)-1):
    for j in range(0, len(stacks)):
        stacks[j] = stacks[j]+init_lines[i][column_numbers[j]]
        stacks[j] = stacks[j].strip()
# Start reading the movement instructions and move boxes around
line = data.readline()
counter = 0
while (line):# and (counter < 5):
    #numbers = list(filter(str.isdigit, line))
    numbers = list(map(int, re.findall(r'\d+', line)))
    no_boxes = int(numbers[0])
    stack_source = int(numbers[1])-1
    stack_target = int(numbers[2])-1
    # These are the boxes that will be moved
    boxes_to_move = stacks[stack_source][0:no_boxes]
    # Remove the boxes from the original stack
    stacks[stack_source] = stacks[stack_source][no_boxes:]
    # Move the boxes on to the new stack in reversed order
    # Change to boxes_to_move[::-1] for task one, this is for task two
    stacks[stack_target] = boxes_to_move[::1] + stacks[stack_target]
    line = data.readline()
    print(stacks)
    counter += 1
ans = ""
for stack in stacks:
    if len(stack) > 0:
        ans = ans+stack[0]
    else:
        ans = ans + ""
print(ans)