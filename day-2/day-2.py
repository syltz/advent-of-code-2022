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
    
def score_eval_top_secret(opp, res):
    score = 0
    # Key = result (loss/draw/win), value = points (0/3/6)
    result_dict = {"X":0, "Y":3, "Z":6}
    # Key = input move, value = numerical value for that move (r/p/s), (1/2/3)
    move_num = {"A":1, "B":2, "C":3}
    result = result_dict[res]
    opp_move = move_num[opp]
    if result == 3:
        # We have a draw
        my_move = opp_move
    elif result == 0:
        # We have a loss 
        # If opp_move = rock, my_move = scissors
        if opp_move == 1:
            my_move = opp_move + 2
        # If opp_move = paper/scissor my_move = rock/paper
        else:
            my_move = opp_move - 1
    else:
        # We have a win
        if opp_move == 3:
            my_move = opp_move - 2
        else:
            my_move = opp_move + 1
    score = result + my_move
    return score

# input_file is the file to read data from
# opt_strat is bool, if True uses opt_strat from task 2, else strat from task 1
def total_score(input_file, opt_strat):
    score = 0
    data = open(input_file, "r") 
    line = data.readline()

    while line:
        shapes = line.split()
        if opt_strat: # Task 2
            score = score + score_eval_top_secret(shapes[0], shapes[1])
        else: # Task 1
            score = score + score_eval(shapes[0], shapes[1])
        line = data.readline()
    return score

# Task 1:
task_1_score = total_score("input.txt", False)
print("Total score task 1: {}".format(task_1_score))
# Task 2:
task_2_score = total_score("input.txt", True)
print("Total score task 2: {}".format(task_2_score))
