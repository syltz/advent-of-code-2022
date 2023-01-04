def get_ranges(str):
    r1, r2 = str.split(",")
    range1 = [int(i) for i in r1.split("-")]
    range2 = [int(i) for i in r2.split("-")]
    return [range1, range2]

# Checks if range2 is a subset of range1
# Assuming sorted lists
def is_subset(range1, range2):
    if (range2[0] >= range1[0]) and (range2[1] <= range1[1]):
        return True
    else:
        return False
def testing_task1():
    test_cases = ["2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"]
    for case in test_cases:
        ranges = get_ranges(case)
        if is_subset(ranges[0], ranges[1]): 
            print("{} is fully contained in {}".format(ranges[1], ranges[0]))
        elif is_subset(ranges[1],ranges[0]):
            print("{} is fully contained in {}".format(ranges[0], ranges[1]))
        else:
            print("Neither of {} and {} are fully contained in each other".format(
                ranges[0], ranges[1]))

data = open("input", "r")
line = data.readline()
fcp = 0 #fully contained pairs
while line:
    ranges = get_ranges(line)
    if is_subset(ranges[0], ranges[1]) or (is_subset(ranges[1], ranges[0])):
        fcp += 1
    line = data.readline()
print("There are {} fully contained pairs".format(fcp))