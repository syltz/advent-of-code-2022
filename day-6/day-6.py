from collections import Counter
test_input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
"bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

def unique_string(line):
    char_counter = Counter(line)
    for letter, count in char_counter.items():
        if count > 1:
            return False
    return True

def find_marker(line, n):
    for i in range(0, len(line)-n):
        sub_str = line[i:i+n]
        if unique_string(sub_str):
            return i+n


data = open("input", "r")
line = data.readline()
packet = 4
message = 14
print("Marker = {}".format(find_marker(line, packet)))
print("Message = {}".format(find_marker(line, message)))