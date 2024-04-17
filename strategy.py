# the beginning of your strategy
def MyStrategy(r, my_history, op_history, my_score, op_score):
    if r == 0:
        return 1
    if r < 5:
        return op_history[r - 1]
    if r == 5 or r == 6:
	    # if opponent has always cooperated, then defect
        if op_history.count(1) == r:
            return 0
        return op_history[r - 1]
    if r == 7:
        if op_history.count(1) == r:
            return 0
	    # if opponent started to defect, then cooperate
        if op_history.count(0) == 1 and op_history[r - 1] == 0:
            return 1
        return op_history[r - 1]
    if r == 8:
        if op_history.count(1) == r:
            return 0
        # if opponent started to defect, then cooperate
        if op_history.count(0) == 2 and op_history[6:8] == [0, 0]:
            return 1
        return op_history[r - 1]
    if r == 9:
        if op_history.count(1) == r:
            return 0
        # if opponent stopped defecting, then cooperate if ahead in score
        if op_history.count(0) == 2 and op_history[6:9] == [0, 0, 1]:
            if (my_score - op_score > 5):
                return 1
            return 0
        return op_history[r - 1]
# the end of your strategy