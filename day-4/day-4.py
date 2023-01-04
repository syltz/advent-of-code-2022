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
def overlap(range1, range2):
    # range1 = [n_r1, m_r1], range2 = [n_r2, m_r2]
    # if n_r1 <= m_r2 <= m_r1 we have overlap, ex r1=[3,9], r2 = [1,4]
    if (range2[1] >= range1[0]) and (range2[1] <= range1[1]):
        return True
    # if n_r2 <= m_r1 <= m_r2 we have overlap, ex r1=[2,7], r2=[7, 8]
    elif (range1[1] >= range2[0]) and (range1[1] <= range2[1]):
        return True
    else:
        return False

data = open("input", "r")
line = data.readline()
fcp = 0 #fully contained pairs
olp = 0 #overlapping pairs
while line:
    ranges = get_ranges(line)
    if is_subset(ranges[0], ranges[1]) or (is_subset(ranges[1], ranges[0])):
        fcp += 1
    if overlap(ranges[0], ranges[1]):
        olp += 1
    line = data.readline()
print("There are {} fully contained pairs".format(fcp))
print("There are {} overlapping paris".format(olp))