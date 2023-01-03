import numpy as np
cal_curr = 0

def store_max(cal_list, new_cal):
    if new_cal > min(cal_list):
        i = np.argmin(cal_list)
        cal_list[i] = new_cal 
    return cal_list
n = 3 # The top n elves
max_cals = np.zeros(n) # Store the calories for the n top elves
data = open("input.txt", "r")
line = data.readline()
while line:
    line = line.strip()
    if line:
        cal_curr = cal_curr + int(line)
    else:
        max_cals = store_max(max_cals, cal_curr)
        cal_curr = 0
    line = data.readline()


print("Maximum calories: {}", sum(max_cals))