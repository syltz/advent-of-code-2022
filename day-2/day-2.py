# Returns 0 if lost, 3 if drawn, 6 if won
def win_eval(opp, me):
    # This dictionary contains translation from symbol to numerical value
    choice_dict = {"A" : 0, "B" : 1, "C" : 2, "X" : 0, "Y" : 1, "Z" : 2}
    # The keys are the diffs (opp-me), the values are the results of the match
    result_dict = {-2: 0, -1 : 6, 0 : 3, 1 : 0, 2 : 6}
    # Reassign the values to be consistent and numerical
    opp = choice_dict[opp]
    me = choice_dict[me]
    diff = opp - me
    return result_dict[diff]

# Returns the score from a single round
def score_eval(opp, me):
    # Contains the scores for the shapes used
    shape_dict = {"X" : 1, "Y" : 2, "Z" : 3}
    score = shape_dict[me] + win_eval(opp, me)
    return score

total_score = 0
data = open("input.txt", "r") 
line = data.readline()

while line:
    shapes = line.split()
    total_score = total_score + score_eval(shapes[0], shapes[1])
    line = data.readline()

print("Total score: {}".format(total_score))
