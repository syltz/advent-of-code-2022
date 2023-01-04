def get_prio(item):
    # for lower case the priority is the position in the string+1
    # for upper case the priority is the position in the string+1 + 26
    prio_order = "abcdefghijklmnopqrstuvwxyz"
    prio = 0
    if item.isupper():
        prio += len(prio_order)
        item = item.lower()
    prio += (prio_order.index(item) + 1)
    return prio

def split_string(str):
    length = len(str)
    str1 = str[0:length//2]
    str2 = str[length//2: length]
    return [str1, str2]

def overlap(str1, str2):
    ret_str = ""
    # check_str contains already checked chars to no doublecount
    check_str = ""
    for char in str1:
        if char in str2 and char not in check_str:
            ret_str = ret_str + char
        check_str = check_str + char
    return ret_str

def rucksack_overlap_prio(str):
    prio = 0
    str1, str2 = split_string(str)
    rs_ol = overlap(str1,str2) # rs_ol = RuckSack_OverLap
    if rs_ol:
        for char in rs_ol:
            prio += get_prio(char)
    return prio

def badge(str_lst):
    # Overlap between strings 1 and 2, 2 and 3, 3 and 1
    ol_12 = overlap(str_lst[0], str_lst[1])
    ol_23 = overlap(str_lst[1], str_lst[2])
    ol_31 = overlap(str_lst[2], str_lst[0])
    # The overlap between the overlap strings should then yield the badge
    badge = overlap(overlap(ol_12, ol_23), ol_31)
    return badge

data = open("input", "r")
rucksacks = ["", "", ""]
for i in range(0, len(rucksacks)):
    rucksacks[i] = data.readline()
overlap_sum = 0
badge_sum = 0
while rucksacks[0]:
    badge_sum += get_prio(badge(rucksacks).strip())
    for i in range(0, len(rucksacks)):
        overlap_sum += rucksack_overlap_prio(rucksacks[i])
        rucksacks[i] = data.readline()

print("Total overlap sum: {}".format(overlap_sum))
print("Total badge sum: {}".format(badge_sum))
